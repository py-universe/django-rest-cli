from typing import Optional, List
import asyncio

from .base import Base, Startable
from .validator import is_django_project_directory


class StartApp(Base):

    @staticmethod
    async def __start( name: str, directory: Optional[str] = None) -> None:
        what: Startable = Startable.APP
        directive: str = f'start{what.name.lower()}'
        template: str = f'{what.name}_TEMPLATES_DIR'

        await Base.run_cmd_command(
            directive, name, directory, template
        )


    @classmethod
    async def create_multiple_apps(cls, apps: List) -> None:
        # Check if command is executed within a django project directory
        is_django_project_directory()

        funcs = []
        for app in apps:
            funcs.append(
                asyncio.ensure_future(cls.__start(app))
            )
        await asyncio.gather(*funcs)
        