DROP TABLE IF EXISTS utenti;
DROP TABLE IF EXISTS service;
DROP TABLE IF EXISTS carrello;

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
    descrizione TEXT, 
    img TEXT,
    link TEXT
);

CREATE TABLE carrello (
    id INTEGER PRIMARY KEY,
    id_uten INTEGER,
    id_prodotto INTEGER,
    quantita INTEGER,
    prezzo_unitario REAL,
    nome_prodotto TEXT
);


INSERT INTO service (nome, modalit, prezzo, stock, descrizione, img, link)
VALUES ('Prodotto 1', 'in presenza', '50.00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala', 'https://raw.githubusercontent.com/youssouf994/afro/master/afro/static/1.webp', 'video.mp4');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione, img, link)
VALUES ('Prodotto 2', 'in presenza', '50.00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalaladewr1jfberjf ewdiofnew dfnnew cdokknf dkofnwew  alala', 'https://raw.githubusercontent.com/youssouf994/afro/master/afro/static/2.webp', 'video.mp4');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione, img, link)
VALUES ('Prodotto 3', 'in presenza', '50.00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala', 'https://raw.githubusercontent.com/youssouf994/afro/master/afro/static/3.webp', 'video.mp4');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione, img, link)
VALUES ('Prodotto 4', 'in presenza', '50.00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala', 'https://raw.githubusercontent.com/youssouf994/afro/master/afro/static/4.webp', 'video.mp4');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione, img, link)
VALUES ('Prodotto 5', 'in presenza', '50.00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala', 'https://raw.githubusercontent.com/youssouf994/afro/master/afro/static/5.webp', 'video.mp4');

INSERT INTO service (nome, modalit, prezzo, stock, descrizione, img, link)
VALUES ('Prodotto 6', 'in presenza', '50.00', 49, 'Descrizione lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala', 'https://photos.google.com/photo/AF1QipM9zwCs75RFakfhXqZjs7XatgujwWvdzKj0L71z', 'video.mp4');
    
