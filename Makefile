run:
	python src/ruff_in_python/main.py tests/bar.py

lint:
	ruff check . --fix & ruff format .
install:
	pip install -e .

test:
	pytest -vv