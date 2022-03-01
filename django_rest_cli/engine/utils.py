import pathlib
import sys


def print_error_message(error_text: str):
    sys.stderr.write(
        "\n" + error_text + "\n"
    )
    sys.exit(1)


def rename_file(old_name: str, new_name: str, base_dir: pathlib.Path):
        (base_dir / old_name).rename(base_dir / new_name)

