install:
	poetry install
lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest gendiff
test-coverage:
	poetry run pytest --cov=gendiff
