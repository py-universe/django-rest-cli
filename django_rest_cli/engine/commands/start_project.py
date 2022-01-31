from importlib import import_module
import pathlib
import sys
from typing import Optional

from PyInquirer import prompt, print_json
from examples import custom_style_3
from prompt_toolkit.validation import Validator, ValidationError

from .base import start, Startable
from django_rest_cli.engine import validate_name
"""
startproject implementation plan:
- on startproject command with project name
- check if project name is valid. If yes, then
- present user with the option to start project from a default template or manually define their configs

 E.g 
    > start from default template
    > manually define project configs
        add-dotenv(yes/no ): 
        add-django-split-settings(yes/no ):
        add-swagger-docs(yes/no):
        add-django-pytest(yes/no):
        auth: []basic token auth []jwt

        - the presets will then be passed to a function that adds/edits certain files in the
        project, depending on the presets.

basically:
define two functions:
1- collects project presets from the CLI
2- accepts certain presets and edits or adds files to the project based on the preset.
"""
def start_project(name: str, directory: Optional[str] = None):
    validate_name(name)

    template_or_manual = [
        {
            'type': 'list',
            'name': 'user_option',
            'message': 'How do you want to start your project',
            'choices': [
                "use default template(It uses the Django-rest-cookietier template",
                "manually select feaures(Offers more flexibility)"
            ]
        }
    ]

    presets = [
        {
            'type': 'list',
            'name': 'auth',
            'message': 'what authentication scheme?',
            'choices': [
                "basic token auth",
                "jwt",
                "None"
            ]
        },

        {
            'type': "confirm",
            "name": "pytest",
            "message": "Install and setup django-pytest for writing unit tests with Pytest?",
        },

        {
            'type': "confirm",
            "name": "dotenv",
            "message": "Install and Setup dotenv for managing secret keys",
        },

        {
            'type': "confirm",
            "name": "split_settings",
            "message": "Install and Setup django_split_settings for modularizing the settings.py file?",
        },

        {
            'type': "confirm",
            "name": "django_rest_swagger",
            "message": "Install and Setup django_rest_swagger for managing docs",
        },
    ]

    project_style = prompt(template_or_manual, style=custom_style_3)

    if "default" in project_style.get('user_option'):
        print("you selected to use the default template")
    else:
        presets = prompt(presets, style=custom_style_3)
        print_json(presets)
        # print("you selected to use the manual option")
    
    start(Startable.PROJECT, name, directory)
    # follow_up_start_project(name, directory)


def follow_up_start_project(name: str, directory: Optional[str] = None):
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


def rename_file(old_name: str, new_name: str, base_dir: pathlib.Path):
    (base_dir / old_name).rename(base_dir / new_name)
