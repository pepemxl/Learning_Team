.PHONY: build run clean rebuild shell

# Get current user ID and group ID
UID := $(shell id -u)
GID := $(shell id -g)

# Variables
IMAGE_NAME = cpp-python-dll-example
CONTAINER_NAME = cpp-python-container

build:
	docker-compose build

run: build
	docker-compose up

clean:
	docker-compose down --rmi all --volumes --remove-orphans
	sudo rm -rf cpp_libs/lib1/build cpp_libs/lib2/build

rebuild: clean build

shell:
	docker-compose run --rm --user "${UID}:${GID}" cpp-python-app /bin/bash

test: build
	docker-compose run --rm --user "${UID}:${GID}" cpp-python-app python3 python_app/main.py

build-cpp-libs:
	docker-compose run --rm --user "${UID}:${GID}" cpp-python-app /bin/bash -c "\
		mkdir -p /app/cpp_libs/lib1/build && \
		cd /app/cpp_libs/lib1/build && \
		cmake .. && \
		make && \
		cd /app/cpp_libs/lib2/build && \
		cmake .. && \
		make"