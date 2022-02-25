from PyInquirer import prompt
from examples import custom_style_3

from django_rest_cli.engine.commands import (
    StartApp,
    StartProject
)
from .mixins import ProjectConfigMixin


class CliCommands(ProjectConfigMixin):

    @staticmethod
    def start_apps(args):
        StartApp.create_multiple_apps(args.apps)
        
    @staticmethod
    def start_project(args):
        mode = ProjectConfigMixin.template_or_manual()
        print(f"mode: {mode}")
        StartProject.start_project(args.project_name, mode)
