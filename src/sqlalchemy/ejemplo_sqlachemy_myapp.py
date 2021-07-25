# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:28:03 2021

@author: Pepe
"""

import ejemplo_sqlachemy_db as db
from ejemplo_sqlalchemy_data_model import CTablaEjemplo

def crea_base_de_datos(Base, engine):
    Base.metadata.create_all(engine)



def test():
    persona1 = CTablaEjemplo('Ernesto', 'Trujillo')
    db.session.add(persona1)
    db.session.commit()

if __name__=='__main__':
    print('Hola Mundo de los ORMs')
    Base = db.Base
    engine = db.engine
    crea_base_de_datos(Base, engine)
    test()