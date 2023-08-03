from flask import Flask
from flask import render_template, redirect, request, url_for
import bcrypt
import sqlite3
import secrets


app = Flask(__name__)
app.secret_key='super_secret_key'

DATABASE = 'archivio_utenti.db'

def db_utenti():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def controllo_user():
        if 'user_id' not in session:
            return redirect(url_for('main'))
        user_id=session['user_id']
        return user_id






    #------------------------------------------------------------------------


"""
wsgi_app = app.wsgi_app

usa la stringa sopra se usi un server http diverso da flask
"""

@app.route('/')
def index():
    """Renders a sample page."""
    return render_template('index.html')


@app.route('/registrazione')
def crea_utente():
    if request=='post':
        id=request.form['#']
        nome=request.form['#']
        cognome=request.form['#']
        tel=request.form['#']
        citta=request.form['#']
        mail=request.form['#']
        passw=request.form['#']

        cursore=db_utenti().cursor()

        cursore.execute('SELECT * FROM utenti WHERE cell=?', (tel,))
        if cursore.fetchone() is not None:
            return redirect(url_for('#'))
        else:
            #-----------CODIFICA VALORI INSERITI--------------
            pass_codificata=bcrypt.haspw(passw.encode('utf-8'), bcrypt.gensalt())
            mail_codificata=bcrypt.haspw(mail.encode('utf-8'), bcrypt.gensalt())
            tel_codificata=bcrypt.haspw(tel.encode('utf-8'), bcrypt.gensalt())
            city_codificata=bcrypt.haspw(citta.encode('utf-8'), bcrypt.gensalt())
            cognome_codificata=bcrypt.haspw(cognome.encode('utf-8'), bcrypt.gensalt())
            nome_codificata=bcrypt.haspw(nome.encode('utf-8'), bcrypt.gensalt())
            id_codificata=bcrypt.haspw(id.encode('utf-8'), bcrypt.gensalt())
            #-----------------------------------------------------------

            cursore.execute('INSERT INTO utenti(id_utenti, nome, cognome, mail, citta, cell, passwo) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (id, nome, cognome, tel, mail, citta, passw ))
            
            db_utenti().commit()
            return redirect(url_for('#'))



"""
    MODIFICARE IL CODICE SOTTOSTANTE PRIMA DI ESEGUIRE IL DEBUG IN PARTICOLARE IL NUMERO DELLA PORTA.
    DOVREBBE ESSERE app.run(host='0.0.0.0', port=xxxx)
"""

if __name__ == '__main__':#parte esecuzione dal file non da codice importato da altro file
    import os#libreria che mi da accesso alle variabili d'ambiente del sist operativo
    HOST = os.environ.get('SERVER_HOST', 'localhost')#prendo la var che contiene host
    try:
        PORT = int(os.environ.get('SERVER_PORT', '4000'))#provo a connettermi alla seguente
    except ValueError:
        PORT = 4000#se c'è un errore passo alla seguente
    app.run(HOST, PORT)#app.run finalizza il codice soprastante
