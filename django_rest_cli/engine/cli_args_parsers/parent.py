import argparse

class ParentArgsParser(object):

    def __init__(self):
        self.parent_parser = argparse.ArgumentParser(prog="drf-cli")


class ActionArgsParser(ParentArgsParser):

    def __init__(self):
        super().__init__()
        
        self.action_parser = self.parent_parser
        
        self.action_parser.add_argument(
            "action", 
            type=str, 
            help="what action to be performed: 'startproject', 'startapp"
        )
        
        # This is an optional arg passed when creating an app in a project
        # It accepts multiple app names
        self.action_parser.add_argument(
            "apps", 
            nargs='*' ,#  Accept multiple app names
            help="name(s) of app(s) to be created'",
            default=None # If no app name is passed, defaults to None
        )
        
        self.args = self.action_parser.parse_args()