from flask import Flask, request, session
 
app = Flask(__name__)
app.secret_key = "123456789"


@app.route('/')
def home():
    # Obtenemos la session
    if 'username' in session:
        username = session['username']
    else:
        username = "usuario anonimo"
    if username is not None:
        return "<h1>Bienvenido " + username + "</h1>"
    return "<h1>Application example of Sessions use</h1>"


@app.route('/setsession')
def setsession():
    session['username'] = 'Pepe'
    return "The session has been Set"
 
@app.route('/getsession')
def getsession():
    if 'username' in session:
        username = session['username']
        return "Bienvenido {0}".format(username)
    else:
        return "Session anonima"
 
@app.route('/popsession')
def popsession():
    session.pop('username', None)
    return "Session Borrada"

app.run(debug=True, host='localhost', port=5000)