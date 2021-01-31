
.PHONY: static-checks test lint check-format

static-checks: test lint check-format

test:
	pipenv run python -m unittest discover

lint:
	pipenv run pylint --fail-under=9 poker
	pipenv run pylint --fail-under=9 test

check-format:
	pipenv run black --check .

report-coverage:
	pipenv run coverage run --source=poker,test -m unittest discover
	pipenv run coverage report -m 