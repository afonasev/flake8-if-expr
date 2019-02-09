import pytest
from flake8_plugin_utils import get_error

from flake8_if_expr import IfExprFound, IfExprPlugin

IF_EXPR = 'x = 1 if 2 else 3'


@pytest.mark.parametrize(
    'src',
    (
        # if expr
        IF_EXPR,
        # noqa for other error code
        f'{IF_EXPR}  # noqa:T100',
    ),
)
def test_error_exists(tmpdir, src):
    assert get_error(IfExprPlugin, tmpdir, src)


@pytest.mark.parametrize(
    'src',
    (
        # empty code
        '',
        # normal if stmt
        'if x:\n    x = 1',
        # noqa
        f'{IF_EXPR}  # noqa',
        # noqa for certain error code
        f'{IF_EXPR}  # noqa:{IfExprFound.code}',
    ),
)
def test_error_not_exists(tmpdir, src):
    assert not get_error(IfExprPlugin, tmpdir, src)
