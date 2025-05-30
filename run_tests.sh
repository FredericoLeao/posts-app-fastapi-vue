#!/bin/bash

# Para e remove containers e imagens, caso existam/estejam executando
docker stop postsapp-db-testing
docker rm postsapp-db-testing
docker rmi postsapp-db-testing
docker stop postsapp-be-testing
docker rm postsapp-be-testing
docker rmi postsapp-be-testing
docker network rm postsapp-network-testing

# Cria network para os containers
docker network create postsapp-network-testing

#########################
# Criar imagens
docker build -t postsapp-be-testing -f Dockerfile.backend .
docker build -t postsapp-db-testing -f Dockerfile.db .


# Cria e executa o container para Backend
docker run -d --network-alias postsapp-be-testing \
    --name postsapp-be-testing --volume=.:/app \
    --network postsapp-network-testing \
    -e 'DATABASE_URL=postgresql://pguser:pgpass@postsapp-db-testing:5432/postsapp-testing' \
    postsapp-be-testing

# Criar e executa o container para DB
docker run -d --network-alias postsapp-db-testing \
    --name postsapp-db-testing --volume=./pgdata-testing:/var/lib/postgres/data \
    --network postsapp-network-testing \
    postsapp-db-testing

# Para adicionar a lógica de aguardar o serviço do container subir
# será necessário alterar o entrypoint para executar o rm e a criação
# do arquivo de "flag container services starting done"
echo "Aguardando inicialização dos serviços"
sleep 4;

# Inicializa base de dados e executa os testes
docker exec -it postsapp-db-testing dropdb postsapp-testing -U pguser;
docker exec -it postsapp-db-testing createdb postsapp-testing -U pguser;
docker exec -it postsapp-be-testing alembic upgrade head;
docker exec -it postsapp-be-testing pytest -vvv;


# Para e remove containers e imagens
docker stop postsapp-db-testing
docker rm postsapp-db-testing
docker rmi postsapp-db-testing
docker stop postsapp-be-testing
docker rm postsapp-be-testing
docker rmi postsapp-be-testing
docker network rm postsapp-network-testing