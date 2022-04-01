import enum
import subprocess
import sys
from typing import Optional, List

from django_rest_cli.engine import paths


@enum.unique
class Startable(enum.Enum):
    PROJECT: int = 0
    APP: int = 1


@enum.unique
class StartType(enum.Enum):
    TEMPLATE: int = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    MANUAL: int = 1


class Base(object):

    @staticmethod
    def run_cmd_command(
        directive: str, name: str, directory: str, template: str
    ) -> None:
        cmd: List[str]
        cmd = ['django-admin', directive, name]

        if directory is not None:
            cmd.append(directory)

        cmd.extend(['--template', str(getattr(paths, template))])

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError:
            sys.exit(1)