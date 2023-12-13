create schema if not exists test;

drop table if exists test.users;

create table if not exists test.users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    company_name VARCHAR(100),
    address VARCHAR(100),
    city VARCHAR(50),
    state CHAR(2),
    zip VARCHAR(10),
    phone1 VARCHAR(20),
    phone2 VARCHAR(20),
    email VARCHAR(100),
    department VARCHAR(50)
 );