BIN = .venv/bin/
CODE = flake8_if_expr

init:
	python3 -m venv .venv
	poetry install

test:
	$(BIN)pytest -vv --cov=$(CODE) $(args)

lint:
	$(BIN)flake8 --jobs 4 --statistics --show-source $(CODE) tests
	$(BIN)pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	$(BIN)mypy $(CODE) tests
	$(BIN)black --skip-string-normalization --line-length=79 --check $(CODE) tests

pretty:
	$(BIN)isort --apply --recursive $(CODE) tests
	$(BIN)black --skip-string-normalization --line-length=79 $(CODE) tests
	$(BIN)unify --in-place --recursive $(CODE) tests

precommit_hook:
	echo '#!/bin/sh\nmake lint test\n' > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

ci: lint test
ci: $(BIN)codecov
