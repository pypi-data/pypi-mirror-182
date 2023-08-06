#!/usr/bin/env python3

"""
This script simply wraps terragrunt (which is a wrapper around terraform...) and its main function is
to allow you to execute a `run-all` command but broken up in individual steps.

This makes debugging a complex project easier, such as spotting where the exact problem is.
"""

# Todo: parse output
# - https://github.com/bcochofel/terraplanfeed/tree/main/terraplanfeed

import os
import sys
import subprocess
import shlex
import json
import re
import click
import networkx as nx

from outdated import check_outdated # type: ignore

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = '0.0.0 '

class Printer():
    """ A simple class for printing nice messages """
    def __init__(
        self,
        verbose: bool,
        ):

        self.verbose = verbose

    def print_header(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho('\n' + msg, bold=True, file=sys.stderr)

    def print_verbose(self, msg):
        if self.verbose:
            msg = msg.strip() if isinstance(msg, str) else msg
            print(msg, flush=True, file=sys.stderr)

    def print_normal(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        print(msg, flush=True, file=sys.stderr)

    def print_bold(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho('\n' + msg, bold=True, file=sys.stderr)

    def print_warning(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho('\n' + msg + '\n', fg="yellow", bold=True, file=sys.stderr)

    def print_error(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho(msg, fg="red", bold=True, file=sys.stderr)

    def print_success(self, msg):
        msg = msg.strip() if isinstance(msg, str) else msg
        click.secho(msg, fg="green", bold=True, file=sys.stderr)

class TgWrap():
    SEPARATOR=':|:'

    def __init__(self, verbose):
        self.printer = Printer(verbose)

        self.check_latest_version()

        # Check if the "TERRAGRUNT_SOURCE" environment variable is set
        env_var = "TERRAGRUNT_SOURCE"
        if env_var in os.environ:
            self.printer.print_warning(f"'{env_var}' environment variable is set with address: '{os.environ[env_var]}'!")
        else:
            self.printer.print_warning(f"No '{env_var}' variable is set, so the sources as defined in terragrunt.hcl files will be used as is!")

    def check_latest_version(self):
        pass
        # check for newer versions
        # try:
        #     is_outdated, latest_version = check_outdated('tgwrap', __version__)
        #     if is_outdated:
        #         click.echo(
        #             f'Your local version ({__version__}) is out of date! Latest is {latest_version}!'
        #         )
        # except ValueError:
        #     # this happens when your local version is ahead of the pypi version,
        #     # which happens only in development
        #     pass

    def prepare_groups(self, graph, exclude_external_dependencies):
        groups = []
        for group in nx.topological_generations(graph):
            try:
                group.remove("\\n") # terragrunt is adding this in some groups for whatever reason
            except ValueError as e:
                pass
            for idx, dir in enumerate(group):
                if dir.startswith("/") \
                    and exclude_external_dependencies \
                    and dir != os.getcwd():
                    self.printer.print_verbose(f"- Remove dir from group as it falls out of scope: {dir}")
                    group[idx] = None
                else:
                    self.printer.print_verbose(f"+ Include dir: {dir}")

            # remove the null values from the list
            group = list(filter(None, group))
            if len(group) > 0:
                groups.append(group)

        return groups

    def get_di_graph(self, terragrunt_args=None):
        "Gets the directed graph by running the `graph-dependencies` command in terragrunt, and parse it into a DG object"
        DG = None
        try:
            temp_file = f'{os.environ["TMPDIR"]}tg-dependencies.gv'
            with open(temp_file, 'w') as f:
                command = f"terragrunt graph-dependencies --terragrunt-non-interactive {' '.join(terragrunt_args)}"
                rc = subprocess.run(
                    shlex.split(command),
                    text=True,
                    stdout=f,
                )
                self.printer.print_verbose(rc)

            # Read the directed graph and reverse it
            DG = nx.DiGraph(nx.nx_pydot.read_dot(temp_file)).reverse()
        except Exception as e:
            self.printer.print_error(e)
            raise click.ClickException(e)

        return DG

    def run_di_graph(self, command, exclude_external_dependencies, dry_run,
        ask_for_confirmation=False, collect_output_file=None, terragrunt_args=None):
        "Runs the desired command in the directories as defined in the directed graph"
        DG = self.get_di_graph(terragrunt_args=terragrunt_args)

        # first go through the groups and clean up where needed
        groups = self.prepare_groups(graph=DG, exclude_external_dependencies=exclude_external_dependencies)

        if ask_for_confirmation or self.printer.verbose:
            self.printer.print_header(f"The following groups will be processed:")
            for idx, group in enumerate(groups):
                self.printer.print_normal(f"\nGroup {idx}:")
                for dir in group:
                    self.printer.print_normal(f"- {dir}")

        if ask_for_confirmation:
            response = input("\nDo you want to continue? (y/n) ")
            if response.lower() != "y":
                sys.exit(1)

        stop_processing = False
        for idx, group in enumerate(groups):
            self.printer.print_header(f'Group {idx}')
            self.printer.print_normal(group)

            if command:
                for dir in group:
                    self.printer.print_header(f'\n\nStart processing directory: {dir}\n\n')
                    if dry_run:
                        self.printer.print_warning(f'In dry run mode, no real actions are executed!!')
                    else:
                        try:
                            if collect_output_file:
                                collect_output_file.write(f'{dir}{self.SEPARATOR}')
                                collect_output_file.flush()
                            temp_file = f'{os.environ["TMPDIR"]}tgwrap-error'
                            messages = ""
                            with open(temp_file, 'w') as f:
                                rc = {'returncode': 0}
                                rc = subprocess.run(
                                    shlex.split(command),
                                    text=True,
                                    cwd=dir,
                                    stdout=collect_output_file if collect_output_file else sys.stdout, # is this really useful? Can be omitted?
                                    stderr=f,
                                )
                                self.printer.print_verbose(rc)

                            with open(temp_file, 'r') as f:
                                messages = f.read()
                            if rc.returncode != 0 or 'error' in messages.lower():
                                raise Exception("An error situation detected while processing the terragrunt graph.")
                        except FileNotFoundError as fnfe:
                            self.printer.print_warning(f"Directory {dir} not found, continue")
                        except Exception as e:
                            self.printer.print_error(f"Error occurred:\n{str(e)}")
                            self.printer.print_error("Full stack:")
                            self.printer.print_normal(messages)

                            stop_processing = True
                            break

            if stop_processing:
                break

    def construct_command(self, command, debug, exclude_external_dependencies, non_interactive=True, no_auto_approve=True, no_lock=True, update_source=False, terragrunt_args=()):
        """ Constructs the command """
        commands = {
            'generic': '{base_command} {command} --terragrunt-non-interactive {no_auto_approve} {ignore_deps} {debug_level} {update_source} {terragrunt_args}',
            'plan': '{base_command} {command} --terragrunt-non-interactive  -out=planfile {ignore_deps} {debug_level} {lock_level} {update_source} {terragrunt_args}',
            'apply': '{base_command} {command} {non_interactive} {no_auto_approve} --terragrunt-parallelism 1 {ignore_deps} {debug_level} {update_source} {terragrunt_args}',
            'show': '{base_command} {command} --terragrunt-non-interactive {ignore_deps} {update_source} -json planfile',
            'destroy': '{base_command} {command} --terragrunt-non-interactive --terragrunt-no-auto-approve {ignore_deps} {debug_level} {terragrunt_args}',
        }

        lock_stmt         = '-lock=false' if no_lock else ''
        update_stmt       = '--terragrunt-source-update' if update_source else ''
        ignore_deps_stmt  = '--terragrunt-ignore-external-dependencies' if exclude_external_dependencies else ''
        debug_stmt        = '--terragrunt-log-level debug --terragrunt-debug' if debug else ''
        auto_approve_stmt = '--terragrunt-no-auto-approve' if no_auto_approve else ''
        interactive_stmt  = '--terragrunt-non-interactive' if non_interactive else ''

        base_command      = 'terragrunt run-all'

        if command not in ['clean']:
            full_command = commands.get(command, commands.get('generic')).format(
                base_command=base_command,
                command=command,
                lock_level=lock_stmt,
                update_source=update_stmt,
                ignore_deps=ignore_deps_stmt,
                debug_level=debug_stmt,
                no_auto_approve=auto_approve_stmt,
                non_interactive=interactive_stmt,
                terragrunt_args=' '.join(terragrunt_args),
            )
        else:
            full_command = commands.get(command, commands.get('generic'))

        # remove double spaces
        full_command = re.sub(' +', ' ', full_command)

        self.printer.print_verbose(f"Full command to execute:\n$ {full_command}")

        return full_command

    def run(self, command, debug, dry_run, no_lock, update_source, auto_approve, terragrunt_args):
        """ Executes a terragrunt command on a single project """

        self.printer.print_verbose(f"Attempting to 'run {command}'")
        if terragrunt_args:
            self.printer.print_verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        if not os.path.isfile("terragrunt.hcl"):
            self.printer.print_error("terragrunt.hcl is not found, this seems not to be a terragrunt project directory! Exit.")
            sys.exit(1)

        cmd = self.construct_command(
            command=command,
            debug=debug,
            exclude_external_dependencies=True,
            no_lock=no_lock,
            update_source=update_source,
            no_auto_approve=False if auto_approve else True,
            terragrunt_args=terragrunt_args,
        )

        if dry_run:
            self.printer.print_warning(f'In dry run mode, no real actions are executed!!')
        else:
            rc = subprocess.run(shlex.split(cmd))
            self.printer.print_verbose(rc)

    def run_all(self, command, debug, dry_run, no_lock, update_source, exclude_external_dependencies, step_by_step, terragrunt_args):
        """ Executes a terragrunt command across multiple projects """

        self.printer.print_verbose(f"Attempting to 'run-all {command}'")
        if terragrunt_args:
            self.printer.print_verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        cmd = self.construct_command(
            command=command,
            debug=debug,
            exclude_external_dependencies=True if step_by_step else exclude_external_dependencies,
            non_interactive=False if command in ['apply', 'destroy'] else True,
            no_lock=no_lock,
            update_source=update_source,
            no_auto_approve=False,
            terragrunt_args=terragrunt_args,
        )

        if step_by_step:
            self.printer.print_verbose("This command will be executed in each individual project directory!")
            self.run_di_graph(
                command=cmd,
                exclude_external_dependencies=exclude_external_dependencies,
                dry_run=dry_run,
            )
        else:
            if dry_run:
                self.printer.print_warning(f'In dry run mode, no real actions are executed!!')
            else:
                rc = subprocess.run(shlex.split(cmd))
                self.printer.print_verbose(rc)

    def analyze(self, dry_run, exclude_external_dependencies, terragrunt_args):
        """ Analyzes the plan files """

        self.printer.print_verbose(f"Attempting to 'analyze'")
        if terragrunt_args:
            self.printer.print_verbose(f"- with additional parameters: {' '.join(terragrunt_args)}")

        # first run a 'show' and write output to file
        cmd = self.construct_command(
            command='show',
            exclude_external_dependencies=exclude_external_dependencies,
            debug=False,
            )

        # then run it and capture the output
        temp_file = f'{os.environ["TMPDIR"]}tgwrap-show'
        json_file = f'{os.environ["TMPDIR"]}planfile.json'
        with open(temp_file, 'w') as f:
            self.run_di_graph(
                command=cmd,
                exclude_external_dependencies=exclude_external_dependencies,
                dry_run=dry_run,
                collect_output_file=f,
                terragrunt_args=terragrunt_args,
            )
        
        ts_validation_successful = True
        with open(temp_file, 'r') as f:
            for line in f:
                split_line = line.split(self.SEPARATOR)
                project = split_line[0]
                plan_file = split_line[1]

                self.printer.print_header(f"Analyse project: {project}")

                try:
                    d = json.loads(plan_file)

                    if 'resource_changes' in d and len(d['resource_changes']) > 0:
                        self.printer.print_header('Changes:')

                        changes = False
                        for rc in d['resource_changes']:
                            # check if we do have actual changes
                            actions = rc['change']['actions']
                            if len(actions) == 1 and actions[0] == 'no-op':
                                pass # ignore, just an state change
                            else:
                                self.printer.print_normal(f'- {rc["address"]}: {",".join(actions)}')
                                changes = True

                        if not changes:
                            print('- no real changes detected.')

                    # if so, write to file
                    with open(json_file, 'w') as f:
                        f.write(plan_file)

                    # Check if the "TERRASAFE_CONFIG" environment variable is set
                    env_var = "TERRASAFE_CONFIG"
                    if not env_var in os.environ:
                        self.printer.print_warning(f"{env_var} environment variable is not set, this is required for running the terrasafe command!")
                    else:
                        self.printer.print_header(f"\nRun terrasafe using config {os.environ.get(env_var)}")

                        cmd = f"cat {json_file} | terrasafe --config {os.environ.get('TERRASAFE_CONFIG')}"
                        output = subprocess.run(
                            cmd,
                            shell=True,
                            text=True,
                            capture_output=True,
                            )
                        if output.returncode != 0:
                            ts_validation_successful = False
                            self.printer.print_error(output.stdout)
                        elif '0 unauthorized' in output.stdout:
                            self.printer.print_success(output.stdout)

                except json.decoder.JSONDecodeError as e:
                    raise Exception(f"Planfile for {project} was no proper json, further analysis not possible.")

        if not ts_validation_successful:
            raise Exception("Terrasafe validation failed on one or more projects")
