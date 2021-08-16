#!/bin/bash
echo "$(pwd)/"
docker-compose -f ./docker_base_images/docker-compose.yml build