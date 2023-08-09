from flask import Flask
from flask import render_template, redirect, request, url_for, g, session
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
        database_ram=db_utenti()
        cursore=database_ram.cursor()




def aggiunta_carta(sessione, numero):

    database_ram=db_utenti()
    cursore=database_ram.cursor()

    if sessione is not None:
        cursore.execute('UPDATE utenti SET n_cart=? WHERE id_utente=? ', (numero, sessione))
        database_ram.commit()
        database_ram.close()





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
           return redirect(url_for('no'))
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

            return render_template('index.html')

    return render_template('registrazione.html')


@app.route('/login', methods=['POST', 'GET'])
def accesso():
    if request.method=='POST':
        utente=request.form['user']
        passwd=request.form['pass'].encode('UTF-8')

        database_ram=db_utenti()
        cursore=database_ram.cursor()

        cursore.execute('SELECT * FROM utenti WHERE nome=?', (utente,))
        trovato_nome=cursore.fetchone()

        database_ram.close()
        

    if trovato_nome is not None and bcrypt.checkpw(passwd, trovato_nome[7]):
        session['id_utenti']=trovato_nome[0]
        return render_template('login.html')
    else:
        return redirect(url_for('no'))


@app.route('/presa_carta', methods=['POST', 'GET'])
def carta():
    id=session['id_utenti']
    if request.method=='POST':
        carta=request.form['card']

        aggiunta_carta(id, carta)

        return redirect(url_for('landing'))

    return render_template('carta.html')
        


@app.route('/land')
def landing():
    return render_template('landing_page.html')

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
