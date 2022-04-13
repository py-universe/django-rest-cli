import pathlib
from termcolor import cprint
import colorama
import subprocess
import inflect
from typing import List


def raise_error_message(error_text: str, exception: Exception):
    raise exception(error_text)


def print_exception(exception: Exception):
    text = "\n⚠️" + str(exception) + "\n"
    colorama.init()
    cprint(text, "red", attrs=["blink", "bold"])


def print_success_message(message: str):
    text = "\n🎉" + message + "\n"
    colorama.init()
    cprint(text, "green", attrs=["blink", "bold"])


def rename_file(old_name: str, new_name: str, base_dir: pathlib.Path):
    (base_dir / old_name).rename(base_dir / new_name)


def init_git_repo(project_dir: pathlib.Path):
    cmd: List[str]
    cmd = ["git", "init", project_dir]
    subprocess.run(cmd, check=True)


def pluralize(string):
    """
    pluralizes a string word using a python library, needed for verbose model names and url paths
    """
    pluralizer = inflect.engine()
    return pluralizer.plural(string)
