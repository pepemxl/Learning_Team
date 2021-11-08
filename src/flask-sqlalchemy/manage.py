# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 01:13:10 2021

@author: Pepe
"""


from main import app, db, User, Post, Tag, migrate


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Tag=Tag, migrate=migrate)
