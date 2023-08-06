# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tgwrap', 'tgwrap.lib']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'networkx>=2.8.8,<3.0.0',
 'outdated>=0.2.2,<0.3.0',
 'pydot>=1.4.2,<2.0.0',
 'terrasafe>=0.5.1,<0.6.0']

entry_points = \
{'console_scripts': ['tgwrap = tgwrap.cli:main']}

setup_kwargs = {
    'name': 'tgwrap',
    'version': '0.1.0',
    'description': 'A (terragrunt) wrapper around a (terraform) wrapper around ....',
    'long_description': "# tg-wrap\n\nThis script simply wraps terragrunt (which is a wrapper around terraform, which is a wrapper around cloud APIs, which is...).\n\nWait, why on earth do we need a wrapper for a wrapper (for a wrapper)?\n\nWell, first of all it is pretty opinionated so what works for us, doesn't necessarily work for you.\n\nBut our reasoning for creating this is as follows:\n\n## Less typing\n\nterraform is great, and in combination with terragrunt even more great! But let's face it, terragrunt does not excel in conciseness! The options are pretty long, which leads to lots of typing.\n\n## Testing modules locally\n\nHowever, more importantly, we are heavily utilising [TERRAGRUNT_SOURCE](https://terragrunt.gruntwork.io/docs/features/execute-terraform-commands-on-multiple-modules-at-once/#testing-multiple-modules-locally) when developing.\n\nThe thing is that as long as you use `run-all` you can use one setting for that variable (and set is as an environment variable), while if you run a regular command, you need to specify the full path.\n\nWhich leads to (even) more typing, and worse: chance for errors.\n\nLuckily you can use `run-all` and add the appriopriate flags to ensure it behaves like a regular plan|apply|destroy etc. But again, more typing.\n\nNothing a [bunch a aliases](https://gitlab.com/lunadata/terragrunt-utils/-/blob/main/tg-shell.sh) can't solve though!\n\n## But the original reason was: Errors when using run-all are challenging\n\nOne of the main boons of terragrunt is the ability to break up large projects in smaller steps while still retaining the inter-dependencies. However, when working on such a large project and something goes wrong somewhere in the middle is pretty challenging.\n\nterragrunt's error messages are pretty massive, and this is extrapolated with every individual project in your dependency chain.\n\nAnd if it fails somewhere at the front, it keeps on trying until the last one, blowing up your terminal in the process.\n\nSo we wanted a possibility to run the projects step by step, using the dependency graph of terragrunt and have a bit more control over it.\n\nThis was not something a bunch of aliases could solve, hence we create this wrapper. And while we we're at it, replacing the aliases with this was then pretty straightforward as well.\n\n## Analyzing plan files\n\nAn important feature is the `tgwrap analyze` function that lists all the planned changes and (if availabe) runs a [terrasafe](https://pypi.org/project/terrasafe/) validation check. It would provide output as follows:\n\n```console\n$ tgwrap analyze -x\n\n...\n\nAnalyse project: inputs\nRun terrasafe: inputs\nConfig loaded from /my/project/dir/terrasafe-config.json\n0 unauthorized deletion detected\n\nAnalyse project: runners\nChanges:\nmodule.vmss.azurerm_key_vault_secret.pwd: delete,create\nmodule.vmss.azurerm_key_vault_secret.user: delete,create\nmodule.vmss.azurerm_linux_virtual_machine_scale_set.this[0]: update\n\nRun terrasafe: runners\nConfig loaded from /my/project/dir/terrasafe-config.json\n0 unauthorized deletion detected\n```\n\n## usage\n\n> Note that it is planned to publish this on pypi.org!\n\n> Note that the dependencies as defined in `requirements.txt` must be availabe.\n\nIt is recommend to 'install' the script in a location included in your `PATH`, for example:\n\n```console\nln -sf ~/git/lunadata/terragrunt-utils/tgwrap/tgwrap.py ~/.local/bin/tgwrap\n```\n\nThen you can run it as follows:\n\n```console\n# general help\ntgwrap --help\n\ntgwrap run -h\ntgwrap run-all -h\n\n# run a plan\ntgwrap plan # which is the same as tgwrap run plan\n\n# run-all a plan\ntgwrap run-all plan\n\n# or do the same in step-by-step mode\ntgwrap run-all plan -s\n\n# or excluding (aka ignoring) external dependencies\ntgwrap run-all plan -sx\n\n# if you want to add additional arguments it is recommended to use -- as separator (although it *might* work without)\ntgwrap output -- -json\n```\n\n## Known limitation\n\ntgwrap does not (in all scenarios) play nice with the `--terragrunt-working-dir` parameter.\n\n## Development\n\nIn order to develop, you need to apply it to your terragrunt projects. For that you can use the `--terragrunt-working-dir` option and just run it from the poetry directory.\n",
    'author': 'Gerco Grandia',
    'author_email': 'gerco.grandia@4synergy.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/lunadata/tgwrap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
