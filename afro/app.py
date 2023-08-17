from flask import Flask
from flask import render_template, redirect, request, url_for, g, session
import bcrypt
import sqlite3
import secrets


app = Flask(__name__)
app.secret_key='super_secret_key'
global id_corso_carrello
global id_utente

DATABASE = 'archivio_utenti.db'

def db_utenti():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


"""def controllo_user():
        database_ram=db_utenti()
        cursore=database_ram.cursor()
"""



def aggiunta_carta(sessione, numero):

    database_ram=db_utenti()
    cursore=database_ram.cursor()

    if sessione is not None:
        cursore.execute('UPDATE utenti SET n_cart=? WHERE id_utente=? ', (numero, sessione))
        database_ram.commit()
        database_ram.close()


def visualizza_tutti_corsi():
    db_ram=db_utenti()
    cursore=db_ram.cursor()

    cursore.execute('SELECT * FROM service')
    corsi=cursore.fetchall()

    db_ram.close()

    return corsi

#-------------------------------------------------------------------------------

def visualizza_un_corso(id):
    db_ram=db_utenti()
    cursore=db_ram.cursor()

    cursore.execute('SELECT * FROM service WHERE id_service=?', (id,))
    corsi=cursore.fetchone()

    db_ram.close()

    return corsi


    #------------------------------------------------------------------------


def elimina_riga(db_ram, id, tabella, colonna):
    """la funzione non apre il database perchè verrebbe già aperto dalla funzione
    db_utenti, quindi passo l'oggetto come parametro e lo utilizzo direttamente"""
    
    try:
        cursore=db_ram.cursor()

        cursore.execute(f"DELETE FROM {tabella} WHERE {colonna}=?", (id,))
        db_ram.commit()
        
        return True

    except Exception as e:
        return render_template("no.html")


#----------------------------------------------------------------------------

def modifica_elemento(db_ram, id, tabella, colonna, nuovo):
    try:
        cursore=db_ram.cursor()

        cursore.execute(f"UPDATE FROM {tabella} SET {colonna}=?, WHERE {id}=?", (nuovo, id))
        db_ram.commit()
        
        return True

    except Exception as e:
        return render_template("no.html")

#------------------------------------------------------------------------------

def aggiungi_corso(db_ram, tabella, nome, mod, prezzo, descrizione ):
    try:
        cursore=db_ram.cursor()

        cursore.execute(f"INSERT INTO {tabella} (nome, modalit, prezzo, stock, descrizione) VALUES (?, ?, ?, ?, ?)", (nome, mod, prezzo, descrizione))
        db_ram.commit()
        
        return True

    except Exception as e:
        return render_template("no.html")


"""
wsgi_app = app.wsgi_app

usa la stringa sopra se usi un server http diverso da flask
"""


@app.route('/no', methods=['POST', 'GET'])
def no():
    return render_template('no.html')


@app.route('/presa_carta', methods=['POST', 'GET'])
def carta():
    id=session['id_utenti']
    if request.method=='POST':
        carta=request.form['card']

        aggiunta_carta(id, carta)

        return redirect(url_for('landing'))

    return render_template('carta.html')


@app.route('/')
def index():
    """Renders a sample page."""
    return render_template('index.html')


@app.route('/reg')
def pag_registrazione():
    return render_template('registrazione.html')



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
    global id_utente
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
        id_utente=session['id_utenti']
        return redirect(url_for('landing'))
    else:
        return redirect(url_for('no'))        


@app.route('/land', methods=['POST', 'GET'])
def landing():
    corsi=visualizza_tutti_corsi()

    return render_template('landing_page.html', corso_singolo=corsi)


@app.route('/cucina_africana/<int:id_corso>')
def panoramica(id_corso):
    global id_corso_carrello
    corso=visualizza_un_corso(id_corso)
    id_corso_carrello=id_corso
    return render_template('pano.html', corso=corso)


@app.route('/carrello', methods=['POST', 'GET'])
def carrello():
    global id_corso_carrello
    global id_utente
    
    if request.method=='POST':
        quant=request.form['quanti']


    if 'id_utenti' in session and id_corso_carrello != None:
        dati = db_utenti()
        cursore = dati.cursor()
        try:
            #prendi il oprezzo dalla tabella corsi
            cursore.execute('SELECT prezzo FROM service WHERE id_service=?', (id_corso_carrello,))
            prezzo=cursore.fetchone()[0]
            

            #Inserisci il corso e i dati nel carrello dell'utente
            cursore.execute('INSERT INTO carrello (id_prodotto, id_uten, quantita, prezzo_unitario) VALUES (?, ?, ?, ?) ', (id_corso_carrello, id_utente, quant, prezzo,))
            dati.commit()

        except Exception as e:
            print("Errore durante l'inserimento nel carrello:", str(e))
            dati.rollback()
        finally:
            dati.close()


        # Resetta le variabili globali
        #id_corso_carrello = None
        #id_utente = None

        return render_template('login.html')
    else:
        return "Errore: ID corso o ID utente mancanti."


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
