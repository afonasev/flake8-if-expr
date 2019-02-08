import ast
import re
from typing import List, Tuple

__version__ = '0.1.1'

ERROR_CODE = 'KEK100'
ERROR_MSG = f'{ERROR_CODE} don`t use "[on_true] if [expression] else [on_false]" syntax'
NOQA_REGEXP = re.compile(r'#.*noqa\s*($|[^:\s])', re.I)
NOQA_WITH_ERROR_CODE_REGEXP = re.compile(r'#.*noqa\s*:\s*' + ERROR_CODE, re.I)


class IfExprFinder(ast.NodeVisitor):
    def __init__(self):
        self.entries: List[Tuple[int, int]] = []

    def visit_IfExp(self, node: ast.AST):  # noqa:N802
        self.entries.append((node.lineno, node.col_offset))


class IfExprChecker:
    name = 'flake8-if-expr'
    version = __version__

    def __init__(self, tree: ast.AST, filename: str):
        self._tree: ast.AST = tree
        self._filename: str = filename
        self._lines: List[str] = []

    def run(self):
        if not self._tree or not self._lines:
            self._load_file()

        visitor = IfExprFinder()
        visitor.visit(self._tree)

        for lineno, col_offset in visitor.entries:
            line = self._lines[lineno - 1]
            if NOQA_REGEXP.search(line):
                continue
            if NOQA_WITH_ERROR_CODE_REGEXP.search(line):
                continue
            yield lineno, col_offset, ERROR_MSG, IfExprChecker

    def _load_file(self):
        with open(self._filename) as f:
            self._lines = f.readlines()
        self._tree = ast.parse(''.join(self._lines))
