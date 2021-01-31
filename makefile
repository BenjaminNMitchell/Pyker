
.PHONY: static-checks test lint check-format

static-checks: test lint check-format

test:
	pipenv run python -m unittest discover

lint:
	pipenv run pylint --fail-under=9 poker
	pipenv run pylint --fail-under=9 test

check-format:
	pipenv run black --check .