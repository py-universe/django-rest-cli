from typing import Optional, List
from .base import Base, Startable


class StartApp(Base):

    @staticmethod
    def _start( name: str, directory: Optional[str] = None) -> None:
        what = Startable.APP
        directive = f'start{what.name.lower()}'
        template = f'{what.name}_TEMPLATES_DIR'

        Base.run_cmd_command(
            directive, name, directory, template
        )


    @classmethod
    def create_multiple_apps(cls, apps: List) -> None:
        for app in apps:
            cls._start(app) # apps created in the directory where command is invoked