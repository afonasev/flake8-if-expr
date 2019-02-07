import pytest

from flake8_if_expr import IfExprChecker


@pytest.mark.parametrize(
    ('src', 'expect_error'),
    (
        # empty code
        ('', False),
        # if stmt
        ('if x:\n    x = 1', False),
        # if expr
        ('x = 1 if 2 else 3', True),
        # noqa
        ('x = 1 if 2 else 3  # noqa', False),
    ),
)
def test_true(tmpdir, src, expect_error):
    path = tmpdir.join('code.py')
    path.write(src)
    has_error = bool(list(IfExprChecker(None, path).run()))
    assert has_error is expect_error
