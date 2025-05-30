#!/bin/bash

# Para e remove os containers, as imagens, e a rede, caso existam
docker stop postsapp-be
docker rm postsapp-be
docker rmi postsapp-be
docker stop postsapp-db
docker rm postsapp-db
docker rmi postsapp-db
docker network rm postsapp-network

# Cria as imagens
docker build -t postsapp-be -f Dockerfile.backend .
docker build -t postsapp-db -f Dockerfile.db .

# Cria rede para os containers
docker network create postsapp-network

# Cria e executa o container para Backend
docker run -d --network-alias postsapp-be \
    --name postsapp-be --volume=.:/app \
    --network postsapp-network -p 8000:8000 \
    -e 'DATABASE_URL=postgresql://pguser:pgpass@postsapp-db:5432/postsapp' \
    postsapp-be


# Criar e executa o container para DB
docker run -d --network-alias postsapp-db \
    --name postsapp-db --volume=./pgdata:/var/lib/postgres/data \
    --network postsapp-network \
    postsapp-db
