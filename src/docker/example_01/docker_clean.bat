@ECHO OFF
ECHO "Remove Container"
ECHO "docker container rm [OPTIONS] CONTAINER [CONTAINER...]"
ECHO "docker rm [OPTIONS] CONTAINER [CONTAINER...]"
ECHO "docker rmi [OPTIONS] IMAGE [IMAGE...]"
ECHO "docker image rm [OPTIONS] IMAGE [IMAGE...]"
docker container rm  docker-example-01
docker image rm docker/example_01:latest
