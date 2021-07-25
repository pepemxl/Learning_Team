# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:18:18 2021

@author: Pepe
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///ejemplo_neto.sqlite')
#connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
MiVariable=5



if __name__=='__main__':
    pass
    #Base.metadata.create_all(engine)