#!/bin/bash


SCHEMA='test'
TABLE='users'
CSV_PATH='/users_data.csv'


COLUMNS='first_name, last_name, company_name, address, city, state, zip, phone1, phone2, email, department'


SQL="\copy ${SCHEMA}.${TABLE}(${COLUMNS}) FROM '${CSV_PATH}' DELIMITER ',' CSV HEADER;"


PGPASSWORD="$POSTGRES_PASSWORD" psql -h "${POSTGRES_HOST}" -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" -c "$SQL"
