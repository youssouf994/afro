DROP TABLE IF EXISTS utenti;
DROP TABLE IF EXISTS service;

CREATE TABLE utenti
(
    id_utente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cognome TEXT,
    mail TEXT,
    citta TEXT,
    cell TEXT,
    n_cart VARCHAR[255],
    passwo VARCHAR[255] NOT NULL
);

CREATE TABLE service
(
	id_service INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    modalit TEXT,
    prezzo DECIMAL(10, 2),
    stock INT,
    descrizione TEXT
);

INSERT INTO service (nome, modalit, prezzo, stock, descrizione)
VALUES ('Prodotto 1', 'in presenza', '50,00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione)
VALUES ('Prodotto 2', 'in presenza', '50,00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione)
VALUES ('Prodotto 3', 'in presenza', '50,00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione)
VALUES ('Prodotto 4', 'in presenza', '50,00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione)
VALUES ('Prodotto 5', 'in presenza', '50,00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione)
VALUES ('Prodotto 6', 'in presenza', '50,00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala');
    
