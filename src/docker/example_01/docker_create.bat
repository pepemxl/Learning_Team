@ECHO OFF
ECHO "Create Container from Image"
ECHO "docker container create [OPTIONS] IMAGE [COMMAND] [ARG...]"
REM --expose Expose a port or a range of ports
REM --mount Attach a filesystem mount to the container
REM --name Assign a name to the container
REM --net Connect a container to a network
REM --rm Automatically remove the container when it exits
REM --volume , -v Bind mount a volume
REM --workdir , -w Working directory inside the container
docker create -p 8080:5000 --name docker-example-01 docker/example_01:latest