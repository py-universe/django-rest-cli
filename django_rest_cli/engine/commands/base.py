import enum
import subprocess
import sys
import pathlib
from typing import Optional, List

from django_rest_cli.engine import paths, rename_file
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

    devs should be able to add dependencies separately through add commands
    E.g drf add dotenv pytest drf_spectacular

    Blocker: How do I add dependencies to a new project
    - adding a dependency entails:
    Approach one:  adding dependency files, and editing necessary files
    Approach two: store dependency files as sub folders and each time the 
    dependency is selected, pick the dependency files from the folder and add
    it to the project.

    for auth, split-settings, basically packages that reuire multiple files,
    we'd use a template folder. for single file or no file deps, we will create the file
    and make neccessary modifications

    How to add deps to requirements.txt file... pip install the specified dependency
    and pip freeze the requirements to the pip file

    Breaking it down to sub problems. What does adding a dependency entails?
    - adding the dependency required files.
    - adding the dependency settings
    - adding the dependency to the requirements.txt file
    - Installing it to the user's virtual env
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

    @staticmethod
    def _follow_up_start_project(name: str, directory: Optional[str] = None):
        if directory is None:
            manage_dir = pathlib.Path('.') / name
        else:
            manage_dir = pathlib.Path(directory)

        manage_dir.resolve(strict=True)
        name_change_map = {
            'secrets.py': '.env',
            'gitignore.py': '.gitignore',
            'requirements.py': 'requirements.txt',
        }

        for (old_name, new_name) in name_change_map.items():
            rename_file(old_name, new_name, base_dir=manage_dir)

    @classmethod
    def start_project(
        cls,
        name: str,
        starttype: StartType,
        directory: Optional[str] = None, 
        presets: Optional[dict] = None, 
    ) -> None:
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

        #d Do something with the presets here
        # cls._follow_up_start_project(name)

    @classmethod 
    def start_app(
        cls,
        name: str,
        directory: Optional[str] = None, 
    ) -> None:
        what = Startable.APP
        directive = f'start{what.name.lower()}'
        template = f'{what.name}_TEMPLATES_DIR'

        cls._run_cmd_command(
            directive, name, directory, template
        )
