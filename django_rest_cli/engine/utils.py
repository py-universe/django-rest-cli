import pathlib
import sys


def raise_error_message(error_text: str, exception: Exception):
    raise exception(error_text)


def rename_file(old_name: str, new_name: str, base_dir: pathlib.Path):
        (base_dir / old_name).rename(base_dir / new_name)

def print_exception(exception: Exception):
    print("\n" + str(exception) + "\n")
    # sys.exit()


def print_success_message(message: str):
    print("\n" + message + "\n")


