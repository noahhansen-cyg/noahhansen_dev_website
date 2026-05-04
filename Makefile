.PHONY: run test lint install

run:
	FLASK_ENV=development .venv/bin/flask --app wsgi run

test:
	.venv/bin/pytest tests/ -v --cov=app --cov-report=term-missing --cov-fail-under=85

lint:
	.venv/bin/flake8 app/ tests/ --max-line-length=100

install:
	python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
