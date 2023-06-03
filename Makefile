install:
	poetry install
lint:
	poetry run flake8 app
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=app --cov-report xml
build:
	poetry build
