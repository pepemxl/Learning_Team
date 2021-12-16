@ECHO OFF
REM docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
REM --name Assign a name to the container
REM --net Connect a container to a network
REM --mount Attach a filesystem mount to the container
REM --publish , -p Publish a container's port(s) to the host  <host_port>:<container_port>
REM --rm Automatically remove the container when it exits
REM --volume , -v Bind mount a volume
REM --workdir , -w Working directory inside the container
docker run -p 8080:5000 --rm --name docker-example-01 docker/example_01:latest