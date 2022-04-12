from django_rest_cli.engine.commands import StartApp, StartProject, AddCrud
from .mixins import ProjectConfigMixin
from .input_validators import validate_name, is_django_project_directory
from django_rest_cli.engine import print_exception


class CliCommands(ProjectConfigMixin):
    @staticmethod
    async def start_apps(args) -> None:
        # Check if command is executed within a django project directory
        is_django_project_directory()
        await StartApp.create_multiple_apps(args.apps)

    @staticmethod
    async def start_project(args) -> None:
        project_name: str = args.project_name

        try:
            validate_name(project_name)

            template_type: str = ProjectConfigMixin.template_type()
            await StartProject.start_project(project_name, template_type)

        except Exception as e:
            print_exception(e)

    @staticmethod
    async def add_crud(args) -> None:
        # Check if command is executed within a django project directory
        is_django_project_directory()
        await AddCrud.addcrud_for_multiple_apps(args.apps)
