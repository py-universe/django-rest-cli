from typing import Optional
from .base import start, Startable


def start_apps(name: str, directory: Optional[str] = None):
    start(Startable.APP, name, directory)