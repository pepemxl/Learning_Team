# -*- coding: utf-8 -*-
"""
Example using Jinja2

@author: pepemxl@gmail.com
"""


from jinja2 import Template

name = 'Pepe'
age = 37

tm = """My name is {{ name }} and I am {{ age }}"""
msg = tm.format(name=name, age=age)

print(msg)