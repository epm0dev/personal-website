#!/usr/bin/env bash

echo "SECRET_KEY=$SECRET_KEY" >> /var/app/.env.prd
echo "ALLOWED_HOSTS=$ALLOWED_HOSTS" >> /var/app/.env.prd
echo "POSTGRES_DB=$POSTGRES_DB" >> /var/app/.env.prd
echo "POSTGRES_USER=$POSTGRES_USER" >> /var/app/.env.prd
echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" >> /var/app/.env.prd
echo "DB_HOST=$DB_HOST" >> /var/app/.env.prd
echo "DB_PORT=$DB_PORT" >> /var/app/.env.prd
echo "REDIS_HOST=$REDIS_HOST" >> /var/app/.env.prd
echo "CORS_ALLOWED_ORIGINS=$CORS_ALLOWED_ORIGINS" >> /var/app/.env.prd
echo "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID" >> /var/app/.env.prd
echo "AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY" >> /var/app/.env.prd