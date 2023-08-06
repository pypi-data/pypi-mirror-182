#!/usr/bin/env python3

import subprocess
from enum import Enum
from typing import Any


class CalledProcessError(RuntimeError):
    """
    A simple exception wrapper for the subprocess.CalledProcessError exception
    """
    def __init__(self, error: subprocess.CalledProcessError):
        self.cmd = error.cmd
        self.retcode = error.returncode
        self.stdout = error.stdout.decode()
        self.stderr = error.stderr.decode()


def run_cmd(command: str, **kwargs: Any) -> str:
    """
    Invoke a process to run the given command.

    :param command: the command to be run
    :param kwargs: any other argument to pass to subprocess.run()
    :returns: standard output of the command or raises a
    CalledProcessError exception
    """
    try:
        cmd_list = command.split()
        p = subprocess.run(
            cmd_list, capture_output=True, check=True, **kwargs
        )

        stdout = p.stdout.decode()

    except subprocess.CalledProcessError as e:
        raise CalledProcessError(e)

    return stdout


class GitEntity(Enum):
    """
    Possible Git entities in the configuration to reference specific
    attributes (e.g., user.name, author.name, user.email, author.email)
    """
    USER = "user"
    AUTHOR = "author"


class ANSIColor(Enum):
    """
    Some useful ANSI color codes
    """
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"


class MessageLevel(Enum):
    """
    Message level prefix messages colored according to their level
    """
    INFO = "[INFO]"
    WARNING = f"{ANSIColor.YELLOW.value}[WARNING]{ANSIColor.END.value}"
    ERROR = f"{ANSIColor.RED.value}[ERROR]{ANSIColor.END.value}"


def context_print(msg_level: MessageLevel, msg: str) -> None:
    """
    Print with the message level prefixed to the given string.

    :param msg_level: the message level prefix of the given string
    :param msg: the given message to be printed
    """
    print(f"{msg_level.value} {msg}")
