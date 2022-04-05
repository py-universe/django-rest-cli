import sys

from django_rest_cli.engine.commands import (
    StartApp,
    StartProject,
    AddPlugin
)
from .mixins import ProjectConfigMixin
from .input_validators import validate_name
from django_rest_cli.engine import print_exception


class CliCommands(ProjectConfigMixin):

    @staticmethod
    async def add_plugins(args) -> None:
        await AddPlugin.add_plugins(args.plugins)

    @staticmethod
    async def start_apps(args) -> None:
        await StartApp.create_multiple_apps(args.apps)
        
    @staticmethod
    async def start_project(args) -> None:
        project_name: str = args.project_name

        try:
            validate_name(project_name)
        except Exception as e:
            print_exception(e)

        mode: str = ProjectConfigMixin.template_or_manual()
        await StartProject.start_project(project_name, mode)
