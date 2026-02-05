.PHONY: build run clean rebuild shell

# Get current user ID and group ID
UID := $(shell id -u)
GID := $(shell id -g)

# Variables
IMAGE_NAME = cpp-python-dll-example
CONTAINER_NAME = cpp-python-container

build:
	docker-compose build

build-debug:
# Construir mostrando todo el output (incluyendo pwd y comandos RUN)
	docker-compose build --no-cache --progress=plain 2>&1 | tee build.log

run: build
	docker-compose up

clean:
	docker-compose down --rmi all --volumes --remove-orphans
	sudo rm -rf cpp_libs/lib1/build cpp_libs/lib2/build

rebuild: clean build

shell:
	docker-compose run --rm --user "${UID}:${GID}" cpp-python-app /bin/bash

shell2:
	docker run -it --rm --user "${UID}:${GID}" python-cpp_cpp-python-app /bin/bash

test: build
	docker-compose run --rm --user "${UID}:${GID}" cpp-python-app python3 python_app/main.py

build-cpp-libs-old:
	docker-compose run --rm --user "${UID}:${GID}" cpp-python-app /bin/bash -c "\
		mkdir -p /app/cpp_libs/lib1/build && \
		cd /app/cpp_libs/lib1/build && \
		cmake .. && \
		make && \
		cd /app/cpp_libs/lib2/build && \
		cmake .. && \
		make"

build-cpp-libs:
	docker-compose run --rm --user "0:0" cpp-python-app /bin/bash -c "\
		mkdir -p /app/cpp_libs/lib1/build && \
		cd /app/cpp_libs/lib1/build && \
		cmake .. && \
		make && \
		cd /app/cpp_libs/lib2/build && \
		cmake .. && \
		make && \
		cp /app/cpp_libs/lib1/build/libmath_operations.so /usr/local/lib/ && \
		cp /app/cpp_libs/lib2/build/libstring_operations.so /usr/local/lib/ && \
		ldconfig"