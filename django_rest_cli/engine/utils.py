import pathlib
from termcolor import cprint
import colorama


def raise_error_message(error_text: str, exception: Exception):
    raise exception(error_text)
    

def rename_file(old_name: str, new_name: str, base_dir: pathlib.Path):
    (base_dir / old_name).rename(base_dir / new_name)


def print_exception(exception: Exception):
    text = "\n⚠️" + str(exception) + "\n"
    colorama.init()
    cprint(text, "red", attrs=["blink", "bold"])


def print_success_message(message: str):
    text = "\n🎉" + message + "\n"
    colorama.init()
    cprint(text, "green", attrs=["blink", "bold"])
