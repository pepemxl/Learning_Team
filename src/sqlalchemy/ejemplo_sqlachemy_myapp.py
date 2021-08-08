# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:28:03 2021

@author: Pepe


TODO:
    - Crear funcion insert de un usuario a la base de datos
    - Crear funcion que pueda borrar usuarios con (nombre, apellido)
    - Crear funcion que pueda leer todos los usuarios con cierto nombre
    - Crear funcion que pueda leer todos los usuarios con cierto apellido
"""

import ejemplo_sqlachemy_db as db
from ejemplo_sqlalchemy_data_model import CTablaEjemplo
from sqlalchemy import and_

def crea_base_de_datos(Base, engine):
    Base.metadata.create_all(engine)

def insert_user(db, nombre, apellido):
    usuario = CTablaEjemplo(nombre, apellido)
    db.session.add(usuario)
    db.session.commit()

def delete_user(db, nombre, apellido):
    try:
        db.session.query(CTablaEjemplo).filter_by(nombre=nombre, apellido=apellido).delete()
        db.session.commit()
    except:
        print('An exception occurred while deleting user')


def read_users_by_name(db, name):
    users = db.session.query(CTablaEjemplo).filter_by(nombre=name).all()
    return users

def read_users_by_last_name(db, last_name):
    users = db.session.query(CTablaEjemplo).filter_by(apellido=last_name).all()
    return users

def test():
    persona1 = CTablaEjemplo('Ernesto', 'Trujillo')
    db.session.add(persona1)
    db.session.commit()

if __name__=='__main__':
    print('Hola Mundo de los ORMs')
    Base = db.Base
    engine = db.engine
    crea_base_de_datos(Base, engine)
    #test()
    #insert_user(db, 'Rosco', 'Perez')
    #insert_user(db, 'Rosco', 'Lopez')
    #insert_user(db, 'Rosco', 'Ramirez')
    #delete_user(db, 'Rosco', 'Lopez')
    users = read_users_by_name(db, 'Rosco')
    print(users)
    users = read_users_by_last_name(db, 'Perez')
    print(users)
    delete_user(db, 'George', 'Pratt')