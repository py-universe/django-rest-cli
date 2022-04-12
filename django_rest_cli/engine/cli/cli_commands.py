from django_rest_cli.engine.commands import StartApp, StartProject, AddCrud
from .mixins import ProjectConfigMixin
from .input_validators import validate_name
from django_rest_cli.engine import print_exception


class CliCommands(ProjectConfigMixin):
    @staticmethod
    async def start_apps(args) -> None:
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
        await AddCrud.addcrud_for_multiple_apps(args.apps)
