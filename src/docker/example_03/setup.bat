@ECHO OFF
docker-compose down --volumes
docker network create -d bridge da_network
docker-compose build
docker-compose up -d

