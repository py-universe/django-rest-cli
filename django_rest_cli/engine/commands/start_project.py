from typing import Optional

from .base import Base, StartType
from django_rest_cli.engine.cli import ProjectConfigMixin


class StartProject(ProjectConfigMixin, Base):

    @classmethod
    def start_project(
        cls, 
        project_name: str, 
        mode: str,
        directory: Optional[str] = None,
    ) -> None:
        
        if "default template" in mode:
             Base.start_project(
                project_name, 
                StartType.TEMPLATE,
                directory,
            )

        else:
            presets = ProjectConfigMixin.project_configs()
            Base.start_project(
                project_name,
                StartType.MANUAL,
                directory,
                presets
            )
