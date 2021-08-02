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
#from sqlalchemy import select, update, delete, values

def crea_base_de_datos(Base, engine):
    Base.metadata.create_all(engine)

def inserta_usuario(nombre, apellido):
    usuario = CTablaEjemplo(nombre, apellido)
    db.session.add(usuario)
    db.session.commit()

def borra_usario(nombre, apellido):
    #usuario = CTablaEjemplo.query.filter_by(nombre=nombre_, apellido=apellido_).first()
    #query = 'select * from ejemplo01 where nombre=\"' + nombre + '\" and apellido=\"' + apellido + '\"'
    query = 'delete from ejemplo01 where nombre=\"' + nombre + '\" and apellido=\"' + apellido + '\"'
    db.engine.execute(query)
    #db.session.delete(usuario)
    #db.session.commit()

def lee_usuarios_x_nombre(nombre):
    query = 'select * from ejemplo01 where nombre=\"' + nombre + '\"'
    res = db.engine.execute(query)
    usuarios = []
    for record in res:
        usuarios.append(record)
        print(record)
    return usuarios

def lee_usuarios_x_apellido(apellido):
    query = 'select * from ejemplo01 where apellido=\"' + apellido + '\"'
    res = db.engine.execute(query)
    usuarios = []
    for record in res:
        usuarios.append(record)
        print(record)
    return usuarios    

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
    #inserta_usuario('Pedro', 'Perez')
    #inserta_usuario('Jorge', 'X')
    #inserta_usuario('Juan', 'Y')
    #borra_usario('Jorge', 'X')
    lee_usuarios_x_nombre('Pedro')
    lee_usuarios_x_apellido('Trujillo')