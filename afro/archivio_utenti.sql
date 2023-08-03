DROP TABLE IF EXISTS utenti;

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
