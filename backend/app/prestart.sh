#!/bin/bash

# Let the DB start
sleep 10;

# Run migrations
alembic upgrade head
