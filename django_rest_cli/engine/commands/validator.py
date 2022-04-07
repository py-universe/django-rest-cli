import os
from pathlib import Path
from pathlib import Path

from django_rest_cli.engine import raise_error_message


def is_django_project_directory():
    cwd: Path = Path.cwd()
    file: Path = cwd / "manage.py"

    if file not in cwd.iterdir():  # manage.py file in current directory?
        error_text: str = (
            "Command Failed. Make sure to execute command in a Django project directory"
        )
        raise_error_message(error_text)
