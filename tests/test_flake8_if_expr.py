import pytest

from flake8_if_expr.checker import ERROR_CODE, IfExprChecker

IF_EXPR = 'x = 1 if 2 else 3'


@pytest.mark.parametrize(
    ('src', 'expect_error'),
    (
        # empty code
        ('', False),
        # if stmt
        ('if x:\n    x = 1', False),
        # if expr
        (IF_EXPR, True),
        # noqa
        (f'{IF_EXPR}  # noqa', False),
        # noqa for certain error code
        (f'{IF_EXPR}  # noqa:{ERROR_CODE}', False),
        (f'{IF_EXPR}  # noqa: {ERROR_CODE}', False),
        (f'{IF_EXPR}  # noqa : {ERROR_CODE}', False),
        # noqa with other comments
        (f'{IF_EXPR}  # pylint:disable NOQA bla bla', False),
        # noqa for other error code
        (f'{IF_EXPR}  # noqa:T100', True),
        (f'{IF_EXPR}  # noqa: T100', True),
        (f'{IF_EXPR}  # noqa : T100', True),
    ),
)
def test_checker(tmpdir, src, expect_error):
    path = tmpdir.join('code.py')
    path.write(src)
    has_error = bool(list(IfExprChecker(None, path).run()))
    assert has_error is expect_error
