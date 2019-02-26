import pytest
from flake8_plugin_utils import assert_error, assert_not_error

from flake8_if_expr import IfExprFinder, IfExprFound


@pytest.mark.parametrize('src', ('x = 1 if 2 else 3',))
def test_error_exists(src):
    assert_error(IfExprFinder, src, IfExprFound)


@pytest.mark.parametrize(
    'src',
    (
        # empty code
        '',
        # normal if stmt
        'if x:\n    x = 1',
    ),
)
def test_error_not_exists(src):
    assert_not_error(IfExprFinder, src)
