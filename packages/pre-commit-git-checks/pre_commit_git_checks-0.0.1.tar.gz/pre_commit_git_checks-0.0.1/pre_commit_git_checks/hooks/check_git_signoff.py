#!/usr/bin/env python3

import re
import sys

from pre_commit_git_checks.hooks.utils import (
    CalledProcessError,
    GitEntity,
    MessageLevel,
    context_print,
    run_cmd,
)


def get_name_config(global_scope: bool, entity: GitEntity) -> str:
    """
    Get the Git configuration for the name attribute.
    Prints the appropriate message if something does not seem as it should be.

    :param global_scope: if True it refers to the global configuration,
    otherwise it refers to the repository local configuration
    :param entity: the type of user for which we want the configuration
    :returns: the output of the git name config command that has run
    """
    scope = "local"
    if global_scope:
        scope = "global"

    std_output = run_cmd(f"git config --{scope} {entity.value}.name")
    name_length = len(std_output.split())

    if name_length < 2:
        context_print(
            MessageLevel.WARNING,
            f"{entity.value}.name is less than two words. Typical format " +
            "is: 'Your Name'"
        )

    return std_output.strip()


def get_email_config(global_scope: bool, entity: GitEntity) -> str:
    """
    Get the Git configuration for the email attribute.

    :param global_scope: if True it refers to the global configuration,
    otherwise it refers to the repository local configuration
    :param entity: the type of user for which we want the configuration
    :returns: the output of the git email config command that has run
    """
    scope = "local"
    if global_scope:
        scope = "global"

    std_output = run_cmd(f"git config --{scope} {entity.value}.email")

    return std_output.strip()


def email_is_valid(email: str) -> bool:
    """
    Check if the email given matches a standard email regex.
    Prints the appropriate message if something does not seem as it should be.

    :param email: the email to be checked
    :returns: True if the email matches the regex, False otherwise
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        return True

    else:
        context_print(
            MessageLevel.WARNING,
            f"{email} does not look like a valid email address."
        )
        return False


def commit_message_is_valid(
    commit_message: str, name: str, email: str
) -> bool:
    """
    Check if a commit message is signed off with the given name and email.
    Prints the appropriate message if something does not seem as it should be.

    :param commit_message: the commit message to be submitted
    :param name: the Git name that should be in the signoff
    :param email: the Git email that should be in the signoff
    :returns: True if the commit message has the correct signoff format,
    False otherwise
    """
    email_is_valid(email)

    expected_sign_off_text = f"Signed-off-by: {name} <{email}>"
    if expected_sign_off_text in commit_message:
        return True

    else:
        context_print(
            MessageLevel.ERROR,
            f"Sign-off message expected to be '{expected_sign_off_text}'."
        )
        context_print(
            MessageLevel.INFO,
            "Check your current Git configuration (`git config -l`) and " +
            "run `git commit --signoff` to signoff."
        )

        return False


def check_git_signoff() -> None:
    """
    Check if a commit message is valid according to the current Git user name
    and email configuration.
    """

    # Checking first the local user name configuration and if it's not set
    # falling back to the global configuration
    user_name = None
    try:
        user_name = get_name_config(global_scope=False, entity=GitEntity.USER)

    except CalledProcessError:
        pass

    if not user_name:
        try:
            user_name = get_name_config(
                global_scope=True, entity=GitEntity.USER
            )

        except CalledProcessError as error:
            context_print(
                MessageLevel.ERROR,
                f"user.name cannot be currently found. {error.stderr}"
            )

    # Checking first the local user email configuration and if it's not set
    # falling back to the global configuration
    user_email = None
    try:
        user_email = get_email_config(
            global_scope=False, entity=GitEntity.USER
        )

    except CalledProcessError:
        pass

    if not user_email:
        try:
            user_email = get_email_config(
                global_scope=True, entity=GitEntity.USER
            )

        except CalledProcessError as error:
            context_print(
                MessageLevel.ERROR,
                f"user.email cannot be currently found. {error.stderr}"
            )

    # Checking both user name and user email and then if needed exiting (error
    # and/or warning message(s) will already have been shown)
    if not (user_name and user_email):
        sys.exit(1)

    # Checking if the commit message has the right format according to the
    # current user name and email configuration

    # https://git-scm.com/docs/git-log#Documentation/git-log.txt-emBem
    git_commit_message = run_cmd("git log --format=%B -n 1")
    if not commit_message_is_valid(git_commit_message, user_name, user_email):
        sys.exit(1)


if __name__ == "__main__":
    check_git_signoff()
