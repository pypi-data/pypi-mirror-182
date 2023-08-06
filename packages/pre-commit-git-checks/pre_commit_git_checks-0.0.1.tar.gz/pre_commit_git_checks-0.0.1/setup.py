# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pre_commit_git_checks', 'pre_commit_git_checks.hooks']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['pgchecks = pre_commit_git_checks.cli:cli']}

setup_kwargs = {
    'name': 'pre-commit-git-checks',
    'version': '0.0.1',
    'description': 'A series of basic Git checks meant for linting of your work.',
    'long_description': '*********************\npre-commit-git-checks\n*********************\n\nA series of basic Git checks meant for linting of your work.\n\n.. contents::\n   :depth: 3\n\nInstallation\n============\nThis tool can be installed as a Python package or a pre-commit hook.\n\nPython package\n--------------\n\nInstall using ``pip`` with:\n\n.. code:: shell\n\n    pip install pre-commit-git-checks\n\npre-commit hook\n---------------\n`pre-commit <https://pre-commit.com/#intro>`_ is a framework that is used for the\nautomated identification of issues in software.\n\n``pre-commit-git-checks`` can be run as a Git hook script before submitting\nyour code.\n\nTo install ``pre-commit`` follow the steps `here <https://pre-commit.com/#install>`__.\n\nYou can see how to integrate a specific hook in the section below.\n\nUsage\n=====\n\nPython CLI\n--------------\nYou can run this tool from the command line.\n\nTo see the help dialog:\n\n.. code:: shell\n\n    $ pgchecks --help\n\n    Usage: pgchecks [OPTIONS] COMMAND [ARGS]...\n\n      A pre-commit checking tool for Git\n\n    Options:\n      --help  Show this message and exit.\n\n    Commands:\n      signoff  Checks your Git commit messages for a signoff\n\nExample usage:\n\n.. code:: shell\n\n    $ pgchecks signoff\n\n    [ERROR] Sign-off message expected to be \'Signed-off-by: Kostas Doe <kdoe@email.com>\'.\n    [INFO] Check your current git configuration (`git config -l`) and run `git commit --signoff` to signoff.\n\nHooks\n-----\n\nIn your ``.pre-commit-config.yaml`` file add:\n\n.. code:: text\n\n    repos:\n      - repo: https://github.com/KAUTH/pre-commit-git-checks\n        rev: master\n        hooks:\n          - id: git-signoff\n            stages: [commit-msg]\n\nTo install the hook(s) run:\n\n* For ``git-signoff``:\n\n.. code:: shell\n\n    pre-commit install --hook-type commit-msg\n\n\n.. note::\n    Running the ``pre-commit install --hook-type <hook-type>`` command will\n    install all the hooks that include in their ``stages`` the ``<hook-type>``\n    value (e.g., ``commit-msg``). Keep in mind that hooks that do not have\n    ``stages`` defined are by default set to all stages, and therefore will\n    always also be installed to the given ``<hook-type>`` as well.\n    You can find more details `here <https://pre-commit.com/#confining-hooks-to-run-at-certain-stages>`_.\n\nTo run individual hooks use:\n\n.. code:: shell\n\n    pre-commit run --hook-stage <stage> <hook_id>\n\ngit-signoff\n~~~~~~~~~~~\nWhat\n""""\nWith the command ``git commit --signoff/-s`` a committer adds a ``Signed-off-by``\ntrailer at the end of the commit log message.\n\nThis hook ensures that the committed message has been signed off with the\ninformation of the Git user.\n\nThe corresponding CLI command ensures that the commit message that is currently\nchecked out has been signed off with the information of the Git user.\n\n.. note::\n    The purpose of this hook is to identify commit messages that have not been\n    explicitly signed off by the committer, and not to automatically add a Signed-off-by\n    line to the message.\n\nWhy\n"""\nAs mentioned in the ``git commit`` `documentation <https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff>`_:\n\n    The meaning of a signoff depends on the project to which you’re committing.\n    For example, it may certify that the committer has the rights to submit the work\n    under the project’s license or agrees to some contributor representation, such as a\n    Developer Certificate of Origin. (See http://developercertificate.org for the one used\n    by the Linux kernel and Git projects.) Consult the documentation or leadership of the\n    project to which you’re contributing to understand how the signoffs are used in that project.\n\nHow\n"""\nThe pre-commit hook and script command checks:\n\n* If a ``user.name`` Git configuration is set at a local level first or a global\n  level and throws an error in the case it is not set in any scope.\n  The same happens for the ``user.email`` configuration.\n\n* If the ``user.name`` configuration resembles the format \'Your Name\' and throws\n  a warning in case it does not.\n\n* If the ``user.email`` configuration resembles the format of an email and\n  throws a warning in case it does not.\n\n* If the Git commit message is singed off with the currently set up ``user.name``\n  and ``user.email`` configurations and throws an error in case it does not.\n\nSign-off message is expected to be: \'Signed-off-by: {user.name} <{user.email}>\'\n\nWhen\n""""\nThe hook runs right after you save your commit message, as a ``commit-msg``\nhook (see https://git-scm.com/docs/githooks#_commit_msg). If the script exits\nnon-zero, Git aborts the commit process.\n\nFor more information check out the ``pre-commit`` documentation, https://pre-commit.com/#pre-commit-for-commit-messages.\n\nLicense\n=======\n`MIT License <https://github.com/KAUTH/pre-commit-git-checks/blob/master/LICENSE>`_',
    'author': 'Konstantinos Papadopoulos',
    'author_email': 'konpap1996@yahoo.com',
    'maintainer': 'Konstantinos Papadopoulos',
    'maintainer_email': 'konpap1996@yahoo.com',
    'url': 'https://github.com/KAUTH/pre-commit-git-checks',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
