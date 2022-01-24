import pathlib
import sys
from typing import Optional

from .base import start, Startable

def start_project(name: str, directory: Optional[str] = None):
    start(Startable.PROJECT, name, directory)
    # follow_up_start_project(name, directory)


def follow_up_start_project(name: str, directory: Optional[str] = None):
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


def rename_file(old_name: str, new_name: str, base_dir: pathlib.Path):
    (base_dir / old_name).rename(base_dir / new_name)
