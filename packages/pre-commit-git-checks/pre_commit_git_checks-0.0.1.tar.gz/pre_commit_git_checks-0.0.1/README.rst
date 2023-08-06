*********************
pre-commit-git-checks
*********************

A series of basic Git checks meant for linting of your work.

.. contents::
   :depth: 3

Installation
============
This tool can be installed as a Python package or a pre-commit hook.

Python package
--------------

Install using ``pip`` with:

.. code:: shell

    pip install pre-commit-git-checks

pre-commit hook
---------------
`pre-commit <https://pre-commit.com/#intro>`_ is a framework that is used for the
automated identification of issues in software.

``pre-commit-git-checks`` can be run as a Git hook script before submitting
your code.

To install ``pre-commit`` follow the steps `here <https://pre-commit.com/#install>`__.

You can see how to integrate a specific hook in the section below.

Usage
=====

Python CLI
--------------
You can run this tool from the command line.

To see the help dialog:

.. code:: shell

    $ pgchecks --help

    Usage: pgchecks [OPTIONS] COMMAND [ARGS]...

      A pre-commit checking tool for Git

    Options:
      --help  Show this message and exit.

    Commands:
      signoff  Checks your Git commit messages for a signoff

Example usage:

.. code:: shell

    $ pgchecks signoff

    [ERROR] Sign-off message expected to be 'Signed-off-by: Kostas Doe <kdoe@email.com>'.
    [INFO] Check your current git configuration (`git config -l`) and run `git commit --signoff` to signoff.

Hooks
-----

In your ``.pre-commit-config.yaml`` file add:

.. code:: text

    repos:
      - repo: https://github.com/KAUTH/pre-commit-git-checks
        rev: master
        hooks:
          - id: git-signoff
            stages: [commit-msg]

To install the hook(s) run:

* For ``git-signoff``:

.. code:: shell

    pre-commit install --hook-type commit-msg


.. note::
    Running the ``pre-commit install --hook-type <hook-type>`` command will
    install all the hooks that include in their ``stages`` the ``<hook-type>``
    value (e.g., ``commit-msg``). Keep in mind that hooks that do not have
    ``stages`` defined are by default set to all stages, and therefore will
    always also be installed to the given ``<hook-type>`` as well.
    You can find more details `here <https://pre-commit.com/#confining-hooks-to-run-at-certain-stages>`_.

To run individual hooks use:

.. code:: shell

    pre-commit run --hook-stage <stage> <hook_id>

git-signoff
~~~~~~~~~~~
What
""""
With the command ``git commit --signoff/-s`` a committer adds a ``Signed-off-by``
trailer at the end of the commit log message.

This hook ensures that the committed message has been signed off with the
information of the Git user.

The corresponding CLI command ensures that the commit message that is currently
checked out has been signed off with the information of the Git user.

.. note::
    The purpose of this hook is to identify commit messages that have not been
    explicitly signed off by the committer, and not to automatically add a Signed-off-by
    line to the message.

Why
"""
As mentioned in the ``git commit`` `documentation <https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff>`_:

    The meaning of a signoff depends on the project to which you’re committing.
    For example, it may certify that the committer has the rights to submit the work
    under the project’s license or agrees to some contributor representation, such as a
    Developer Certificate of Origin. (See http://developercertificate.org for the one used
    by the Linux kernel and Git projects.) Consult the documentation or leadership of the
    project to which you’re contributing to understand how the signoffs are used in that project.

How
"""
The pre-commit hook and script command checks:

* If a ``user.name`` Git configuration is set at a local level first or a global
  level and throws an error in the case it is not set in any scope.
  The same happens for the ``user.email`` configuration.

* If the ``user.name`` configuration resembles the format 'Your Name' and throws
  a warning in case it does not.

* If the ``user.email`` configuration resembles the format of an email and
  throws a warning in case it does not.

* If the Git commit message is singed off with the currently set up ``user.name``
  and ``user.email`` configurations and throws an error in case it does not.

Sign-off message is expected to be: 'Signed-off-by: {user.name} <{user.email}>'

When
""""
The hook runs right after you save your commit message, as a ``commit-msg``
hook (see https://git-scm.com/docs/githooks#_commit_msg). If the script exits
non-zero, Git aborts the commit process.

For more information check out the ``pre-commit`` documentation, https://pre-commit.com/#pre-commit-for-commit-messages.

License
=======
`MIT License <https://github.com/KAUTH/pre-commit-git-checks/blob/master/LICENSE>`_