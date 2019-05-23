import ast

from flake8_plugin_utils import Error, Plugin, Visitor

__version__ = '1.0.0'


class IfExprFound(Error):
    code = 'IF100'
    message = (
        f'{code} don`t use "[on_true] if [expression] else [on_false]" syntax'
    )


class IfExprFinder(Visitor):
    def visit_IfExp(self, node: ast.IfExp) -> None:
        self.error_from_node(IfExprFound, node)


class IfExprPlugin(Plugin):
    name = 'flake8-if-expr'
    version = __version__
    visitors = [IfExprFinder]
