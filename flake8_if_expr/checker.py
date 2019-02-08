import ast
import re
from functools import partial
from typing import Iterable, List, NamedTuple, Optional

__version__ = '0.1.1'

ERROR_CODE = 'KEK100'
ERROR_MSG = f'{ERROR_CODE} don`t use "[on_true] if [expression] else [on_false]" syntax'
NOQA_REGEXP = re.compile(r'#.*noqa\s*($|[^:\s])', re.I)
NOQA_WITH_ERROR_CODE_REGEXP = re.compile(r'#.*noqa\s*:\s*' + ERROR_CODE, re.I)


class Error(NamedTuple):
    lineno: int
    col_offset: int
    message: str
    type: 'IfExprChecker'


class IfExprFinder(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: List[Error] = []

    def visit_IfExp(self, node: ast.IfExp) -> None:  # noqa:N802
        error = KEK100(lineno=node.lineno, col_offset=node.col_offset)
        self.errors.append(error)


class IfExprChecker:
    name = 'flake8-if-expr'
    version = __version__

    def __init__(self, tree: Optional[ast.AST], filename: str) -> None:
        self._tree: Optional[ast.AST] = tree
        self._filename: str = filename
        self._lines: List[str] = []

    def run(self) -> Iterable[Error]:
        if not self._tree or not self._lines:
            self._load_file()

        visitor = IfExprFinder()
        visitor.visit(self._tree)  # type: ignore

        for error in visitor.errors:
            line = self._lines[error.lineno - 1]
            if not self._check_noqa(line):
                yield error

    def _load_file(self) -> None:
        with open(self._filename) as f:
            self._lines = f.readlines()
        self._tree = ast.parse(''.join(self._lines))

    def _check_noqa(self, line: str) -> bool:
        if NOQA_REGEXP.search(line):
            return True
        if NOQA_WITH_ERROR_CODE_REGEXP.search(line):
            return True
        return False


KEK100 = partial(Error, message=ERROR_MSG, type=IfExprChecker)
