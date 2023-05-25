.PHONY: all venv install test

all: venv install test

venv:
 python -m venv venv
 venv/bin/pip install -r requirements.txt

install:
 venv/bin/python setup.py build
 venv/bin/python setup.py install

test:
 venv/bin/python -m pytest tests.py
