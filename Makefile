.PHONY: run lint format typecheck test pre-commit

run:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

lint:
	poetry run ruff check .

lint-fix:
	poetry run ruff check . --fix

format:
	poetry run black .
	poetry run isort .

typecheck:
	poetry run mypy app

test:
	poetry run pytest -v

pre-commit:
	poetry run pre-commit run --all-files
