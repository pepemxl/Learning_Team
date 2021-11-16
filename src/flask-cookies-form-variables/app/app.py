from flask import Flask, make_response, request, render_template
 
app = Flask(__name__)


@app.route('/')
def home():
    # Obtenemos la cookie username
    username = request.cookies.get('username')
    if username is not None:
        return "<h1>Bienvenido " + username + "</h1>"
    #return "<h1>Application example of Cookies use</h1>"
    return render_template('setcookie.html')


@app.route('/setcookieform', methods = ['POST', 'GET'])
def setcookieform():
    if request.method == 'POST':
        username = request.form['nm']
    resp = make_response("The Flask Cookie has been Set for user {0}".format(username))
    resp.set_cookie('username', username)
    return resp

@app.route('/setcookie')
def setcookie():
    resp = make_response("The Flask Cookie has been Set")
    resp.set_cookie('Name','Learning Team')
    return resp


@app.route('/setcookie2')
def setcookie2():
    resp = make_response("The Flask Cookie has been Set")
    resp.set_cookie('username','Pepe')
    return resp

@app.route('/setcookie3')
def setcookie3():
    resp = make_response("The Flask Cookie has been Set")
    resp.set_cookie('Name','Learning Team')
    resp.set_cookie('username','Pepe')
    resp.set_cookie('country','México')
    return resp
 
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('Name')
    if name is None:
        return "The Flask Cookie has not been Set"
    else:
        return "The Site : {0}".format(name)

@app.route('/getcookie2')
def getcookie2():
    username = request.cookies.get('username')
    if username is None:
        return "The Flask Cookie has not been Set"
    else:
        return "username : {0}".format(username)

@app.route('/getcookie3')
def getcookie3():
    name = request.cookies.get('Name')
    username = request.cookies.get('username')
    country = request.cookies.get('country')
    return "Name: {0} Username: {1} Country: {2}".format(name, username, country)

app.run(debug=True, host='localhost', port=5000)