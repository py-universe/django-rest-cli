import enum
import subprocess
import sys
from typing import Optional, List

from django_rest_cli.engine import paths


@enum.unique
class Startable(enum.Enum):
    PROJECT = 0
    APP = 1


def start(what: Startable, name: str, directory: Optional[str] = None):
    directive = f'start{what.name.lower()}'
    cmd: List[str]
    cmd = ['django-admin', directive, name]

    if directory is not None:
        cmd.append(directory)

    templates_dir_name = f'{what.name}_TEMPLATES_DIR'
    cmd.extend(['--template', str(getattr(paths, templates_dir_name))])

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)
