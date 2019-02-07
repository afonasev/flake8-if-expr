BIN = .venv/bin/
CODE = flake8_if_expr

init:
	python3 -m venv .venv
	poetry install

test:
	$(BIN)pytest -vv --cov=$(CODE) $(args)

lint:
	$(BIN)flake8 --jobs 4 --statistics $(CODE) tests
	$(BIN)pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	$(BIN)black --py36 --skip-string-normalization --line-length=79 --check $(CODE) tests

pretty:
	$(BIN)isort --apply --recursive $(CODE) tests
	$(BIN)black --py36 --skip-string-normalization --line-length=79 $(CODE) tests
	$(BIN)unify --in-place --recursive $(CODE) tests

precommit_install:
	echo '#!/bin/sh\nmake lint test\n' > .git/hooks/pre-commit

ci: BIN =
ci: lint test
