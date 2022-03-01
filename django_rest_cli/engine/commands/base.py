import enum
import subprocess
import sys
from typing import Optional, List

from django_rest_cli.engine import paths

"""
    after getting the presets what's next?

    preset:
        - Always add a requirements.txt file to every project
        - Always add setup.cfg file
        - Pytest
            - if yes, add pytest to requirements file
            - update required settings in setup.cfg file

        - dotenv
            - if yes, add dotenv to requirements file
            - add .env file
"""

@enum.unique
class Startable(enum.Enum):
    PROJECT = 0
    APP = 1


@enum.unique
class StartType(enum.Enum):
    TEMPLATE = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    MANUAL = 1


class Base(object):

    @staticmethod
    def run_cmd_command(directive, name, directory, template):
        cmd: List[str]
        cmd = ['django-admin', directive, name]

        if directory is not None:
            cmd.append(directory)

        cmd.extend(['--template', str(getattr(paths, template))])

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError:
            sys.exit(1)