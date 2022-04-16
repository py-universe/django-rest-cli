from importlib import import_module
from pathlib import Path

from django_rest_cli.engine.exceptions import (
    NotDjangoProjectDirectory,
    ProjectAppNameError,
)
from django_rest_cli.engine.utils import raise_error_message


def is_django_project_directory():
    cwd: Path = Path.cwd()
    file: Path = cwd / "manage.py"

    if file not in cwd.iterdir():  # manage.py file in current directory?
        error_text: str = (
            "Command Failed. Make sure to execute command in a Django project directory"
        )
        raise_error_message(error_text, NotDjangoProjectDirectory)


def validate_name(name: str, name_or_dir: str = "name") -> None:
    # Check it's a valid identifier.
    if not name.isidentifier():
        error_text: str = (
            "Invalid project name. Check that the project name is a "
            "valid Python Identifier"
        )
        raise_error_message(error_text, ProjectAppNameError)

    # Check it cannot be imported.
    try:
        import_module(name)
    except ImportError:
        pass
    else:
        error_text: str = (
            f"'{name}' conflicts with the name of an existing Python "
            "module and cannot be used. Please try "
            "another name."
        )
        raise_error_message(error_text, ProjectAppNameError)
