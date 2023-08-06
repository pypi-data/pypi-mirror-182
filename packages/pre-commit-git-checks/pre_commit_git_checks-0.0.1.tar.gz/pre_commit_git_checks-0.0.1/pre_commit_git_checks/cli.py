#!/usr/bin/env python3

import click

from pre_commit_git_checks.hooks.check_git_signoff import check_git_signoff


@click.group(help="A pre-commit checking tool for Git")
def cli():
    """Function to call the pre-commit checking tool as a CLI script"""
    pass


@cli.command(
    help="Checks your Git commit messages for a signoff",
    context_settings=dict(allow_extra_args=True)
)
def signoff():
    """CLI command to check the Git signoff"""
    # we set allow_extra_args to True because when it's invoked as a
    # pre-commit (commit-msg) script, .git/COMMIT_EDITMSG is passed as an
    # argument, which we don't use for now
    check_git_signoff()
