-- Dades de mostra per el programa gestor

-- Inserts per a la taula col_leccions
INSERT INTO col_leccions (nom, descripcio) VALUES ('Pintura', 'Col·lecció de pintures d''artistes diversos');
INSERT INTO col_leccions (nom, descripcio) VALUES ('Escultura', 'Col·lecció de sculptures d''artistes diversos');
INSERT INTO col_leccions (nom, descripcio) VALUES ('Numismàtica', 'Col·lecció de monedes antigues de diversos països');
INSERT INTO col_leccions (nom, descripcio) VALUES ('Documents', 'Col·lecció de documents històrics diversos');

-- Inserts per a la taula autors
INSERT INTO autors (nom, cognoms) VALUES ('Pablo', 'Picasso');
INSERT INTO autors (nom, cognoms) VALUES ('Salvador', 'Dalí');
INSERT INTO autors (nom, cognoms) VALUES ('Joan', 'Miró');
INSERT INTO autors (nom, cognoms) VALUES ('Frida', 'Kahlo');

-- Inserts per a la taula bens_culturals
INSERT INTO bens_culturals (nom, descripcio, data_creacio, id_autor, id_col_leccio) VALUES ('La Gioconda', 'Quadre de Leonardo da Vinci', '1503/01/01', NULL, 1);
INSERT INTO bens_culturals (nom, descripcio, data_creacio, id_autor, id_col_leccio) VALUES ('Guernica', 'Quadre de Pablo Picasso', '1937/01/01)', 1, 1);
INSERT INTO bens_culturals (nom, descripcio, data_creacio, id_autor, id_col_leccio) VALUES ('La persistència de la memòria', 'Quadre de Salvador Dalí', '1931/01/01', 2, 1);
INSERT INTO bens_culturals (nom, descripcio, data_creacio, id_autor, id_col_leccio) VALUES ('La Masia', 'Quadre de Joan Miró', null, 3, 1);
