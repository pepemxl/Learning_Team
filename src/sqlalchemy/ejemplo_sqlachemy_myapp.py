# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:28:03 2021

@author: Pepe


TODO:
    - Crear funcion insert de un usuario a la base de datos
    - Crear funcion que pueda borrar usuarios con (nombre, apellido)
    - Crear funcion que pueda leer todos los usuarios con cierto nombre
    - Crear funcion que pueda leer todos los usuarios con cierto apellido
    - Revisar Docker de flask-celery
"""

import ejemplo_sqlachemy_db as db
from ejemplo_sqlalchemy_data_model import CTablaEjemplo
from sqlalchemy import or_, and_

def crea_base_de_datos(Base, engine):
    Base.metadata.create_all(engine)



def test():
    persona1 = CTablaEjemplo('Ernesto', 'Trujillo')
    db.session.add(persona1)
    db.session.commit()

def test2():
    persona1 = CTablaEjemplo('Pepe', 'Alonzo')
    db.session.add(persona1)
    db.session.commit()
    
    
def insert_db(db, objeto):
    session = db.session
    session.add(objeto) # validacion del tipo de objeto o meter try catch
    db.session.commit()

def delete_db_CTableEjemplo(db, nombre, apellido):
    myquery = db.session.query(CTablaEjemplo).filter_by(and_(nombre=nombre, apellido=apellido)).delete()
    if myquery:
        db.session.commit()
    #myquery = session.query(CTablaEjemplo).filter_by(nombre="Ernesto").first()
#    print(type(myquery))
#    myquery = session.query(CTablaEjemplo).filter(or_(and_(CTablaEjemplo.nombre=="Ernesto",CTablaEjemplo.id==3), CTablaEjemplo.apellido=="Alonzo")).all()
#    print(myquery)
#    myquery = session.query(CTablaEjemplo).filter_by(nombre="Ernesto").all()
#    for item in myquery:
#        print(item)
#    myquery = session.query(CTablaEjemplo).filter_by(or_(nombre="Ernesto", apellido="Alonzo"))
#    myquery = session.query(CTablaEjemplo).filter_by(nombre="Ernesto")
#    print(myquery)
#    res = session.execute(myquery)
#    print(res)
#    for item in res:
#        print(item)
#    res.close()
#    
#    print(type(myquery))
#    res = db.session.commit()
#    print(res)
#    myquery_del = session.query(CTablaEjemplo).filter_by(id=2, nombre='Ernesto').delete()
#    print(myquery_del)
#    db.session.commit()
#    myquery_update = session.query(CTablaEjemplo).filter(and_(CTablaEjemplo.id==5, CTablaEjemplo.nombre=='Hola')).update({'nombre':'Hola2'})
#    print(myquery_update)
#    db.session.commit()
    #res = CTablaEjemplo.select().execute()
    #for row in result:
    #    print(row)
    #res.close()
    #autocommit_engine = eng.execution_options(isolation_level="AUTOCOMMIT")

def holamundo(hola, mundo='jajaja'):
    hola = hola + ' ' + mundo
    print(hola)


if __name__=='__main__':
    print('Hola Mundo de los ORMs')
    Base = db.Base
    engine = db.engine
    hola = 'hola'
    holamundo(hola='jaja')
#    crea_base_de_datos(Base, engine)
#    test()
    #insert_db(db)