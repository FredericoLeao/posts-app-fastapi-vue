#!/bin/bash
docker exec -w /app -it postsapp-be alembic revision --autogenerate -m "$1"
