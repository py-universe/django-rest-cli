from .parent import ParentArgsParser


class StartprojectArgsParser(ParentArgsParser):
    def __init__(self):
        super().__init__(self)
        self.startproject_parser = self.parent_parser
        self.args = self.startproject_parser.parse_args()