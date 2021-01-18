#!/usr/bin/env bash

cd /var/app/ || exit
docker-compose -f docker-compose.prd.yml up --build