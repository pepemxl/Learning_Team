# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:20:10 2021

@author: Pepe
"""


import ejemplo_sqlachemy_db

from sqlalchemy import Column, String, Integer


class CTablaEjemplo(ejemplo_sqlachemy_db.Base):
    __tablename__ = 'ejemplo01'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return "TableEjemplo({0}, {1})".format(self.nombre,self.apellido)

    def __str__(self):
        return self.nombre+self.apellido