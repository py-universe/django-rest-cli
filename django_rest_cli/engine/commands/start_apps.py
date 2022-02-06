from typing import Optional, List
from .base import Base, Startable


class StartApp(Base):

    def start( name: str, directory: Optional[str] = None):
        Base.start_app(name, directory)

    @classmethod
    def create_multiple_apps(cls, apps: List) -> None:
        for app in apps:
            cls.start(app) # apps created in the directory where command is invoked