install:
	poetry install
lint:
	flake8 gendiff
pytest:
	poetry run pytest -vv