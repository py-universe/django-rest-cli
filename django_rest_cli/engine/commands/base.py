import asyncio
import enum
from typing import List

from django_rest_cli.engine import paths
from django_rest_cli.engine.exceptions import CommandError
from django_rest_cli.engine.utils import print_exception, print_success_message


@enum.unique
class Startable(enum.Enum):
    PROJECT: int = 0
    APP: int = 1


class Base(object):
    @staticmethod
    async def run_cmd_command(
        directive: str, name: str, directory: str, template: str
    ) -> None:
        cmd: List[str]
        cmd = ["django-admin", directive, name]

        if directory is not None:
            cmd.append(directory)

        cmd.extend(["--template", str(getattr(paths, template))])

        try:
            cmd = " ".join(cmd)
            proc = await asyncio.create_subprocess_shell(
                cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await proc.communicate()

            if stderr:
                raise CommandError(stderr.strip())
            else:
                print_success_message(f"{name} successfully created\n\n")

        except CommandError as e:
            print_exception(e)
