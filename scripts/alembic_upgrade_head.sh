#!/bin/bash
docker exec -w /app -ti postsapp-be alembic upgrade head
