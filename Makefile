.PHONY: install test test-unit test-live report smoke lint format

install:
	python -m pip install -r requirements.txt

test:
	python -m pytest

test-unit:
	python -m pytest -m "not live"

test-live:
	python -m pytest -m live

report:
	python -m pytest --html=reports/report.html --self-contained-html

smoke:
	python -m pytest -m smoke

lint:
	python -m ruff check .

format:
	python -m ruff format .
