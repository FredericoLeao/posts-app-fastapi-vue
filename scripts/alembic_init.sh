#!/bin/bash
docker exec -w /app -it postsapp-be alembic init migrations
