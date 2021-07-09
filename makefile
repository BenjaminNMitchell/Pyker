
.PHONY: static-checks test lint check-format format

static-checks: test check-format lint check-types

test:
	pipenv run pytest test

lint:
	pipenv run pylint --fail-under=9 poker
	pipenv run pylint --fail-under=9 test

check-format:
	pipenv run black --check .

check-types:
	pipenv run mypy poker

report-coverage:
	pipenv run coverage run --source=poker,test -m unittest discover
	pipenv run coverage report -m 

format:
	pipenv run black .