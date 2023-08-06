# tg-wrap

This script simply wraps terragrunt (which is a wrapper around terraform, which is a wrapper around cloud APIs, which is...).

Wait, why on earth do we need a wrapper for a wrapper (for a wrapper)?

Well, first of all it is pretty opinionated so what works for us, doesn't necessarily work for you.

But our reasoning for creating this is as follows:

## Less typing

terraform is great, and in combination with terragrunt even more great! But let's face it, terragrunt does not excel in conciseness! The options are pretty long, which leads to lots of typing.

## Testing modules locally

However, more importantly, we are heavily utilising [TERRAGRUNT_SOURCE](https://terragrunt.gruntwork.io/docs/features/execute-terraform-commands-on-multiple-modules-at-once/#testing-multiple-modules-locally) when developing.

The thing is that as long as you use `run-all` you can use one setting for that variable (and set is as an environment variable), while if you run a regular command, you need to specify the full path.

Which leads to (even) more typing, and worse: chance for errors.

Luckily you can use `run-all` and add the appriopriate flags to ensure it behaves like a regular plan|apply|destroy etc. But again, more typing.

Nothing a [bunch a aliases](https://gitlab.com/lunadata/terragrunt-utils/-/blob/main/tg-shell.sh) can't solve though!

## But the original reason was: Errors when using run-all are challenging

One of the main boons of terragrunt is the ability to break up large projects in smaller steps while still retaining the inter-dependencies. However, when working on such a large project and something goes wrong somewhere in the middle is pretty challenging.

terragrunt's error messages are pretty massive, and this is extrapolated with every individual project in your dependency chain.

And if it fails somewhere at the front, it keeps on trying until the last one, blowing up your terminal in the process.

So we wanted a possibility to run the projects step by step, using the dependency graph of terragrunt and have a bit more control over it.

This was not something a bunch of aliases could solve, hence we create this wrapper. And while we we're at it, replacing the aliases with this was then pretty straightforward as well.

## Analyzing plan files

An important feature is the `tgwrap analyze` function that lists all the planned changes and (if availabe) runs a [terrasafe](https://pypi.org/project/terrasafe/) validation check. It would provide output as follows:

```console
$ tgwrap analyze -x

...

Analyse project: inputs
Run terrasafe: inputs
Config loaded from /my/project/dir/terrasafe-config.json
0 unauthorized deletion detected

Analyse project: runners
Changes:
module.vmss.azurerm_key_vault_secret.pwd: delete,create
module.vmss.azurerm_key_vault_secret.user: delete,create
module.vmss.azurerm_linux_virtual_machine_scale_set.this[0]: update

Run terrasafe: runners
Config loaded from /my/project/dir/terrasafe-config.json
0 unauthorized deletion detected
```

## usage

> Note that it is planned to publish this on pypi.org!

> Note that the dependencies as defined in `requirements.txt` must be availabe.

It is recommend to 'install' the script in a location included in your `PATH`, for example:

```console
ln -sf ~/git/lunadata/terragrunt-utils/tgwrap/tgwrap.py ~/.local/bin/tgwrap
```

Then you can run it as follows:

```console
# general help
tgwrap --help

tgwrap run -h
tgwrap run-all -h

# run a plan
tgwrap plan # which is the same as tgwrap run plan

# run-all a plan
tgwrap run-all plan

# or do the same in step-by-step mode
tgwrap run-all plan -s

# or excluding (aka ignoring) external dependencies
tgwrap run-all plan -sx

# if you want to add additional arguments it is recommended to use -- as separator (although it *might* work without)
tgwrap output -- -json
```

## Known limitation

tgwrap does not (in all scenarios) play nice with the `--terragrunt-working-dir` parameter.

## Development

In order to develop, you need to apply it to your terragrunt projects. For that you can use the `--terragrunt-working-dir` option and just run it from the poetry directory.
