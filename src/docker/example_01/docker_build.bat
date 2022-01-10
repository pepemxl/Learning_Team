@ECHO OFF
ECHO "Build Template docker-flask-app-example-01"
ECHO "docker build -t <repository>/<project_name>:<version_tag> <location of Dockerfile>"
ECHO "docker build -t docker/example_01:latest ./flask-app"
docker build -t docker/example_01:latest ./flask-app