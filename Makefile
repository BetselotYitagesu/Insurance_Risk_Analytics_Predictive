.PHONY: venv install test clean

venv:
	python3 -m venv venv

install: venv
	venv/bin/pip install -r requirements.txt

test:
	venv/bin/pytest

clean:
	rm -rf venv __pycache__ build dist *.egg-info
