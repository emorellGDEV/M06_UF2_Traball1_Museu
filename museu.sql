CREATE DATABASE museu;

use museu;

CREATE TABLE col_leccions (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) UNIQUE NOT NULL,
    descripcio TEXT
);

CREATE TABLE autors (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    cognoms VARCHAR(50) NOT NULL
);

CREATE TABLE bens_culturals (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    descripcio TEXT,
    data_creacio DATE,
    id_autor INTEGER REFERENCES autors(id),
    id_col_leccio INTEGER REFERENCES col_leccions(id)
);
