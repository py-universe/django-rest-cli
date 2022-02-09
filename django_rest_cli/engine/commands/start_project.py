from typing import Optional

from PyInquirer import prompt, print_json
from examples import custom_style_3
from prompt_toolkit.validation import Validator, ValidationError

from .base import Base, StartType
from django_rest_cli.engine import validate_name


class StartProject(Base):

    @staticmethod
    def _start_project_from_template(directory: str) -> None:
        project_name = [
            {
                'type': 'input',
                'name': 'project_name',
                'message': 'project name must be a valid python variable: ',
                # 'validate': validate_name
            }
        ]

        project_name = prompt(project_name, style=custom_style_3)
        Base.start_project(
            project_name.get('project_name'), 
            StartType.TEMPLATE,
            directory
        )

    @staticmethod
    def _start_project_manually(directory: str) -> None:
        presets = [
            {
                'type': 'input',
                'name': 'project_name',
                'message': 'project name must be a valid python variable: ',
                # 'validate': validate_name,
            },
 
            {
                'type': 'list',
                'name': 'auth',
                'message': 'what authentication scheme? ',
                'choices': [
                    "basic token auth",
                    "jwt",
                    "None"
                ]
            },

            {
                'type': "confirm",
                "name": "pytest",
                "message": "Install and setup django-pytest for writing unit tests with Pytest? ",
            },

            {
                'type': "confirm",
                "name": "dotenv",
                "message": "Install and Setup dotenv for managing secret keys? ",
            },

            {
                'type': "confirm",
                "name": "split_settings",
                "message": "Install and Setup django_split_settings for modularizing the settings.py file? ",
            },

            {
                'type': "confirm",
                "name": "django_rest_swagger",
                "message": "Install and Setup django_rest_swagger for managing docs? ",
            },
        ]
        
        presets = prompt(presets, style=custom_style_3)
        Base.start_project(
            presets.get('project_name'),
            StartType.MANUAL,
            directory
        )

    @classmethod
    def start_project(cls, directory: Optional[str] = None) -> None:
        template_or_manual = [
            {
                'type': 'list',
                'name': 'user_option',
                'message': 'How do you want to start your project: ',
                'choices': [
                    "use default template(It uses the Django-rest-cookietier template. Internet connection required ",
                    "manually select feaures(Offers more flexibility) "
                ]
            }
        ]
        project_style = prompt(template_or_manual, style=custom_style_3)

        if "default" in project_style.get('user_option'):
            cls._start_project_from_template(directory)
        else:
            cls._start_project_manually(directory)