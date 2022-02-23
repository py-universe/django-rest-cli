from PyInquirer import prompt
from examples import custom_style_3
from prompt_toolkit.validation import Validator, ValidationError

from django_rest_cli.engine.commands import (
    StartApp,
    StartProject
)
from django_rest_cli.engine.cli_args_parsers import (
    ActionArgsParser, 
)
from django_rest_cli.engine import print_error_message
from .mixins import ProjectConfigMixin


class Cli(ProjectConfigMixin):

    @staticmethod
    def start_apps(apps):
        StartApp.create_multiple_apps(apps)
        
    @staticmethod
    def start_project(project_name: str):
        mode = ProjectConfigMixin.template_or_manual
        StartProject(project_name, mode)

    @classmethod
    def main(cls):
        action_parser = ActionArgsParser()
        args = action_parser.args

        if args.action == "startapps":
            if args.apps:
               cls.start_apps(args.apps)
            else:
                error_text = f"'{args.action}' expects one or more app names \n E.g. startapps app_1 app_2 app_3\n"
                print_error_message(error_text)

        elif args.action == "startproject":
                project_name = ""
                cls.start_project(project_name)

        elif args.action == "generate-crud-endpoints":
            print("command logic still in the works")

        else:
            error_text = f"'{args.action}' is not a valid action\n" \
                "It should be either 'startapps', 'startproject' or 'generate-crud-endpoints'\n"
            print_error_message(error_text)
