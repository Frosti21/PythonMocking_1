.PHONY: install run test

run:
	python3 main.py

install:
	pip install -r requirements.txt --break-system-packages

test:
	pytest -v
