import pathlib
from typing import Optional

from django_rest_cli.engine.cli.mixins import ProjectConfigMixin
from django_rest_cli.engine.utils import (
    display_project_setup_instructions,
    init_git_repo,
    install_dependencies,
    rename_file,
)

from .base import Base, Startable


class StartProject(ProjectConfigMixin, Base):
    @staticmethod
    def __follow_up_start_project(
        name: str, template_type: str, directory: Optional[str] = None
    ) -> None:
        if directory is None:
            manage_dir: pathlib.Path = pathlib.Path(".") / name
        else:
            manage_dir: pathlib.Path = pathlib.Path(directory)

        manage_dir.resolve(strict=True)
        name_change_map: dict = {
            "secrets.py": ".env",
            "readme.py": "readme.md",
            "setup.py": "setup.cfg",
            "compose.py": "docker-compose.yaml",
        }

        try:
            for (old_name, new_name) in name_change_map.items():
                rename_file(old_name, new_name, base_dir=manage_dir)
        except FileNotFoundError:
            pass

        init_git_repo(manage_dir)
        install_dependencies(manage_dir)
        display_project_setup_instructions(template_type)

    @classmethod
    async def __start(
        cls,
        name: str,
        template_type: str,
        directory: Optional[str] = None,
    ) -> None:
        what: Startable = Startable.PROJECT
        directive: str = f"start{what.name.lower()}"
        template: str = f"{what.name}_TEMPLATE_URL_{template_type.upper()}"

        await Base.run_cmd_command(directive, name, directory, template)
        cls.__follow_up_start_project(name, template_type)

    @classmethod
    async def start_project(
        cls,
        project_name: str,
        template_type: str,
        directory: Optional[str] = None,
    ) -> None:

        await cls.__start(project_name, template_type, directory)
