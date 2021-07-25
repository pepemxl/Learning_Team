# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:23:36 2021

@author: Pepe
"""


from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def home():
    return '<h1>Hello world</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')