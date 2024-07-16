#!/bin/bash

echo "Starting database setup..."

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Создание базы данных
    CREATE DATABASE $TEST_DB;

    -- Создание пользователя
    CREATE USER $TEST_USER WITH PASSWORD '$TEST_PASSWORD';

    -- Подключение к базе данных test_db
    \c $TEST_DB

    -- Предоставление прав пользователю на базу данных
    GRANT ALL PRIVILEGES ON DATABASE $TEST_DB TO $TEST_USER;

    -- Предоставление прав на схему public
    GRANT ALL ON SCHEMA public TO $TEST_USER;

    -- Установка test_user владельцем схемы public
    ALTER SCHEMA public OWNER TO $TEST_USER;

    -- Предоставление прав на создание объектов в схеме public
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO $TEST_USER;
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO $TEST_USER;
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO $TEST_USER;
EOSQL

echo "Database setup completed."