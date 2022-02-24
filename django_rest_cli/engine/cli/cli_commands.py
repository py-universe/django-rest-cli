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
        mode = ProjectConfigMixin.template_or_manual
        StartProject(args.project_name, mode)
