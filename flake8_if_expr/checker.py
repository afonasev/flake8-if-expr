import ast
from typing import List, Tuple

import pycodestyle

IF_EXPR_ERROR_MSG = (
    'KEK100 don`t use "[on_true] if [expression] else [on_false]" syntax'
)


class IfExprFinder(ast.NodeVisitor):
    def __init__(self):
        self.entries: List[Tuple[int, int]] = []

    def visit_IfExp(self, node: ast.AST):  # noqa
        self.entries.append((node.lineno, node.col_offset))


class IfExprChecker:
    name = 'flake8-if-expr'
    version = '0.1.0'

    def __init__(self, tree: ast.AST, filename: str):
        self.tree: ast.AST = tree
        self.filename: str = filename
        self.lines: List[str] = []

    def load_file(self):
        if self.filename in ('stdin', '-', None):
            self.filename = 'stdin'
            self.lines = pycodestyle.stdin_get_value().splitlines(True)
        else:
            self.lines = pycodestyle.readlines(self.filename)

        if not self.tree:
            self.tree = ast.parse(''.join(self.lines))

    def run(self):
        if not self.tree or not self.lines:
            self.load_file()

        visitor = IfExprFinder()
        visitor.visit(self.tree)

        for lineno, col_offset in visitor.entries:
            if not pycodestyle.noqa(self.lines[lineno - 1]):
                yield lineno, col_offset, IF_EXPR_ERROR_MSG, IfExprChecker
