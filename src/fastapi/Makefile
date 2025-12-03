PY := python3.10
VENV := venv
REPONAME=$(basename $(pwd))
PYTHON_VERSION = 3.10

DOCKER=docker
DOCKER_COMPOSE = docker-compose

.PHONY: help
help:
	@echo 
	@echo "- \make install"

example-01:
	uvicorn example_01:app --reload