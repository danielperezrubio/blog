#!/bin/bash

# Let the DB start
sleep 10;

# Run migrations
alembic upgrade head

# Create initial data in DB
python ./app/backend_pre_start.py
