.PHONY: all install tests

all: help


tests:
	pytest tests

install:
	pip install -r requirements.txt


help:
	@echo '----'
	@echo 'tests			  - run tests'
	@echo 'install            - install dependencies'
