@ECHO OFF
REM docker start [OPTIONS] CONTAINER [CONTAINER...]
REM --attach , -a Attach STDOUT/STDERR and forward signals
REM docker build [OPTIONS] PATH | URL | -
REM Build an image from a Dockerfile
REM --label Set metadata for an image
REM --no-cache Do not use cache when building the image
REM --rm true Remove intermediate containers after a successful build
REM --tag , -t Name and optionally a tag in the 'name:tag' format
REM 
REM docker run -p 8080:5000 --name docker-example-01 docker/example_01:latest
REM docker container create [OPTIONS] IMAGE [COMMAND] [ARG...]
docker start docker-example-01
