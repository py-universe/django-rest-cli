import pathlib
import socket
import subprocess
from typing import List

import colorama
import inflect
from termcolor import cprint


def raise_error_message(error_text: str, exception: Exception):
    raise exception(error_text)


def print_exception(exception: Exception):
    text = "\n❌🙁" + "FAILED: " + str(exception) + "\n"
    colorama.init()
    cprint(text, "red", attrs=["blink", "bold"])


def print_success_message(message: str):
    text = "\n⚡🚀 " + "SUCCESS: " + message + "\n"
    colorama.init()
    cprint(text, "green", attrs=["blink", "bold"])


def print_info_message(message: str):
    text = "\n🤓🧠" + "INFO: " + message + "\n"
    colorama.init()
    cprint(text, "yellow", attrs=["blink", "bold"])


def rename_file(old_name: str, new_name: str, base_dir: pathlib.Path):
    (base_dir / old_name).rename(base_dir / new_name)


def init_git_repo(project_dir: pathlib.Path):
    cmd: List[str]
    cmd = ["git", "init", project_dir]
    subprocess.run(cmd, check=True)


def has_internet_connection() -> bool:
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False


def install_dependencies(project_dir: pathlib.Path) -> None:
    if has_internet_connection():
        print_info_message(
            "Internet Connection Detected-- Installing Project Dependencies"
        )

        requirements: pathlib.Path = project_dir / "requirements.txt"
        dev_requirements: pathlib.Path = project_dir / "requirements-dev.txt"

        cmd: List[str]
        cmd = ["pip", "install", "-r", requirements]
        subprocess.run(cmd, check=True)

        if dev_requirements.exists():
            print_info_message("Installing Dev Dependencies")
            cmd: List[str]
            cmd = ["pip", "install", "-r", dev_requirements]
            subprocess.run(cmd, check=True)

        print_info_message("All Project Dependencies Successfully Installed")
    else:
        print_info_message(
            "Tried Installing Project Dependencies, but no Internet Connection Detected."
            "Install Project Dependencies with pip to Finish Setting up this Project.\n"
            "pip install -r requirements.txt"
        )


def setup_precommit_hook(project_dir: pathlib.Path) -> None:
    if has_internet_connection():
        print_info_message(
            "Internet Connection Detected-- Installing git hooks in your project"
        )
    else:
        print_info_message(
            "Tried Installing Git Hooks, but no Internet Connection Detected.\n"
            "Run pre-commit install \n"
            "to Finish Setting up pre-commit hook in this project"
        )


def pluralize(string):
    """
    pluralizes a string word using a python library, needed for verbose model
    names and url paths
    """
    pluralizer = inflect.engine()
    return pluralizer.plural(string)
