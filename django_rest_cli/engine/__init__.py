import asyncio
import platform

from django_rest_cli.engine.cli import main
from django_rest_cli.engine.cli.input_validators import validate_name

from .exceptions import CommandError, NoModelsFoundError, ProjectAppNameError
from .utils import (
    init_git_repo,
    pluralize,
    print_exception,
    print_success_message,
    raise_error_message,
    rename_file,
)


def entry_point():
    if platform.system() == "Windows":  # Had issues with getting it to work on Windows
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())
