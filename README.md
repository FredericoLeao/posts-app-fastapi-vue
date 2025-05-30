# Posts App com FastAPI

## Stack backend e conceitos utilizados

- FastApi com SQLModel, alembic e postgresql

- Implementação de camadas: service e repository

- IO Schemas com Pydantic

- Modulo db para conexão com o banco, utilizando dependency injection

- Testes automatizados em containers separados

## Para executar o projeto

- clone o repositório

- para subir a aplicação execute ```./scripts/docker-run-containers.sh``` 

- para executar testes unitários execute ```./scripts/run_tests.sh```

## Observações

- sobre os testes unitários: sempre vão executar em container separado, com banco de dados próprio, sem depender ou interferir na aplicação principal

- sobre o docker: optei por utilizar os comandos docker diretamente, sem o docker compose, apenas para fins didáticos
