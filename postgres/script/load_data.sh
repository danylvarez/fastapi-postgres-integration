#!/bin/bash

# Configura tus variables
SCHEMA='test'
TABLE='users'
CSV_PATH='/users_data.csv'

# Define las columnas del CSV que se mapearán a la tabla (todas excepto 'id')
COLUMNS='first_name, last_name, company_name, address, city, state, zip, phone1, phone2, email, department'

# Comando SQL para COPY
SQL="\copy ${SCHEMA}.${TABLE}(${COLUMNS}) FROM '${CSV_PATH}' DELIMITER ',' CSV HEADER;"

# Ejecuta el comando
PGPASSWORD="$POSTGRES_PASSWORD" psql -h "${POSTGRES_HOST}" -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "$SQL"
