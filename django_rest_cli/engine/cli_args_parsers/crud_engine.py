from .parent import ParentArgsParser


class CrudengineArgsParser(ParentArgsParser):
    def __init__(self):
        super().__init__(self)
        self.crud_engine_parser = self.parent_parser
        self.args = self.crud_engine_parser.parse_args()