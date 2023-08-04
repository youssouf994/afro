from flask import Flask
from flask import render_template, redirect, request, url_for, g
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


@app.route('/reg')
def pag_registrazione():
    return render_template('registrazione.html')

@app.route('/no', methods=['POST', 'GET'])
def no():
    return render_template('no.html')


@app.route('/registrazione', methods=['POST', 'GET']) 
def crea_utente():
    if request.method=='POST':
        nome=request.form['nome']
        cognome=request.form['cognome']
        tel=request.form['tel']
        citta=request.form['citt']
        mail=request.form['mail']
        passw=request.form['pass']

        data=db_utenti()
        cursore=data.cursor()


        cursore.execute('SELECT * FROM utenti WHERE cell=?', (tel,))
        if cursore.fetchone() is not None:
            return render_template('no.html')
        else:
            #-----------CODIFICA VALORI INSERITI--------------
            pass_codificata=bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
            #mail_codificata=bcrypt.hashpw(mail.encode('utf-8'), bcrypt.gensalt())
            #tel_codificata=bcrypt.hashpw(tel.encode('utf-8'), bcrypt.gensalt())
            #city_codificata=bcrypt.hashpw(citta.encode('utf-8'), bcrypt.gensalt())
            #cognome_codificata=bcrypt.hashpw(cognome.encode('utf-8'), bcrypt.gensalt())
            #nome_codificata=bcrypt.hashpw(nome.encode('utf-8'), bcrypt.gensalt())
            #-----------------------------------------------------------

            cursore.execute('INSERT INTO utenti (nome, cognome, mail, citta, cell, passwo) VALUES (?, ?, ?, ?, ?, ?)',
                            (nome, cognome, mail, citta, tel, pass_codificata ))
            
            data.commit()
            data.close()

            return redirect(url_for('index'))

    return render_template('registrazione.html')


@app.route('/login', methods=['POST', 'GET'])
def accesso():
    if request=='POST':
        utente=request.form['user'].encode('UTF-8')
        passwd=requst.form['pass'].encode('UTF-8')

        database_ram=sqlite3.connect('archivio_utenti.db')
        cursore=database_ram.cursor()

        cursore.execute('SELECT * FROM utenti WHERE nome=?', (utente,))
        trovato_nome=cursore.fetchone()

        cursore.execute('SELECT * FROM utenti WHERE passwo=?', (passwd,))
        trovato_ps=cursore.fetchone()

        database_ram.close()

    if ((trovato_nome is not None and bcrypt.checkpw(utente, trovato_nome[1])) and ( trovato_ps is not None and bcrypt.chekpw (passwd, trovato_ps[7] ) ) ):
          sessione['id_utenti']=trovato_nome[0]
          return redirect(url_for('registrazione'))
    else:
          return redirect(url_for('index'))
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
