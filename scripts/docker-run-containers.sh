#!/bin/bash

# Cria network para os containers
docker network create postsapp-network

# Cria e executa o container para Backend
docker run -d --network-alias postsapp-be --name postsapp-be --volume=.:/app --network postsapp-network -p 8000:8000 postsapp-be

# Criar e executa o container para DB
docker run -d --network-alias postsapp-db --name postsapp-db --volume=./pgdata:/var/lib/postgres/data --network postsapp-network postsapp-db
