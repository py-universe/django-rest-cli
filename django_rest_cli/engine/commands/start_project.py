from typing import Optional
import pathlib

from .base import Base, StartType, Startable
from django_rest_cli.engine.cli import ProjectConfigMixin

from django_rest_cli.engine import rename_file


class StartProject(ProjectConfigMixin, Base):

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
    def _start(
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

        Base.run_cmd_command(
            directive, name, directory, template
        )

        if presets:
            pass
            # Do something with the presets here
            # cls._follow_up_start_project(name)

    @classmethod
    def start_project(
        cls, 
        project_name: str, 
        mode: str,
        directory: Optional[str] = None,
    ) -> None:
        
        if "default template" in mode:
            cls._start(
                project_name, 
                StartType.TEMPLATE,
                directory,
            )

        else:
            presets = ProjectConfigMixin.project_configs()
            cls._start(
                project_name,
                StartType.MANUAL,
                directory,
                presets
            )
