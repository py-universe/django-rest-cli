import enum
import subprocess
import sys
from typing import Optional, List

from django_rest_cli.engine import paths


@enum.unique
class Startable(enum.Enum):
    PROJECT = 0
    APP = 1


@enum.unique
class StartType(enum.Enum):
    TEMPLATE = 0
    MANUAL = 1


class Base(object):

    def _run_cmd_command(directive, name, directory, template):
        cmd: List[str]
        cmd = ['django-admin', directive, name]

        if directory is not None:
            cmd.append(directory)

        cmd.extend(['--template', str(getattr(paths, template))])

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError:
            sys.exit(1)

    @classmethod
    def start_project(
        cls,
        name: str,
        starttype: StartType,
        directory: Optional[str] = None, 
    ):
        what = Startable.PROJECT
        directive = f'start{what.name.lower()}'
        template = None

        if starttype.name.lower() == 'template':
            template = ""
        else:
            template = f'{what.name}_TEMPLATES_DIR'

        cls._run_cmd_command(
            directive, name, directory, template
        )

    @classmethod 
    def start_app(
        cls,
        name: str,
        directory: Optional[str] = None, 
    ):
        what = Startable.APP
        directive = f'start{what.name.lower()}'
        template = f'{what.name}_TEMPLATES_DIR'

        cls._run_cmd_command(
            directive, name, directory, template
        )