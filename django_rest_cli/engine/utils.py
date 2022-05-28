import pathlib
import socket
import subprocess
from typing import List

import colorama
import inflect
from termcolor import cprint

from .enums import Templates


def raise_error_message(error_text: str, exception: Exception):
    raise exception(error_text)


def print_exception(exception: Exception):
    text = "\n❌🙁 " + "FAILED: " + str(exception) + "\n"
    colorama.init()
    cprint(text, "red", attrs=["blink", "bold"])


def print_success_message(message: str):
    text = "\n⚡🚀 " + "SUCCESS: " + message + "\n"
    colorama.init()
    cprint(text, "green", attrs=["blink", "bold"])


def print_info_message(message: str):
    text = "\n🤓🧠 " + "INFO: " + message + "\n"
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


def display_project_setup_instructions(
    template_type: str,
) -> None:
    if Templates.BASIC.value in template_type:
        print_info_message(
            "Project Run Steps:Run the following commands\n\n"
            """pip install -r requirements.txt --Ignore this if dr-cli
            already installed dependencies \n"""
            "python manage.py migrate \n"
            "python manage.py runserver \n"
            "point your browser to `http://localhost:8000/api/v1/docs to view docs \n"
        )

    if Templates.MEDIOR.value in template_type:
        print_info_message(
            "Project Run Steps: Run the following commands:\n\n"
            """pip install -r requirements.txt and
            pip install -r requirements-dev.txt
            --Ignore this if dr-cli installed dependencies \n"""
            "pre-commit install \n"
            "python manage.py makemigrations users \n"
            "python manage.py migrate \n"
            "python manage.py runserver \n"
            "Point your browser to http://localhost:8000/api/v1/docs to view docs \n"
        )

    if Templates.ADV.value in template_type:
        print_info_message(
            "Project Run Steps: Run the following commands\n\n"
            "pre-commit install \n"
            "docker-compose up --build \n"
            "Navigate to your project directory in a new terminal and run:\n\n"
            "docker-compose exec web python manage.py makemigrations users \n"
            "docker-compose exec web python manage.py migrate \n"
            "Point your browser to http://localhost:8000/api/v1/docs to view docs \n"
        )
