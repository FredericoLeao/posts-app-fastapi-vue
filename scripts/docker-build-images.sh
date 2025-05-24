#!/bin/bash

#########################
# Criar imagem para Backend
docker build -t postsapp-be -f Dockerfile.backend .

# Criar imagem para DB
docker build -t postsapp-db -f Dockerfile.db .
