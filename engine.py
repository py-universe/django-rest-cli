import sys


def main():
    try:
        from drf_project_builder.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import drf_project_builder."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
