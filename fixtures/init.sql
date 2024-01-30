-- SQL to initialize local db

CREATE TYPE provider_type AS ENUM ('openai_requests', 'awsbedrock_requests', 'cohere_requests');

CREATE TABLE requests (
    id serial primary key,
    user_input VARCHAR,
    user_email VARCHAR,
    response JSON,
    model VARCHAR,
    temperature FLOAT,
    created_at TIMESTAMP WITHOUT TIME ZONE,
    endpoint VARCHAR,
    extras JSON,
    provider provider_type
);
