# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World GET Services</h1>'

@app.route('/api/v1/query1/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json(silent=True)
    print(content)
    return uuid

@app.route("/api/v1/query2", methods=["GET"])
def starting_url():
    json_data = request.json
    a_value = json_data["a_key"]
    return "JSON value sent: " + a_value

if __name__ == '__main__':
    #app.run(host= '0.0.0.0', debug=True)
    app.run(debug=True, host='localhost', port=5000)