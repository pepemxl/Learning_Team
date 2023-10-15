# -*- coding: utf-8 -*-
"""
Example using Jinja2

@author: pepemxl@gmail.com
"""


from jinja2 import Template

name = 'Pepe'
age = 37

tm = Template("My name is {{ name }} and I am {{ age }}")
msg = tm.render(name=name, age=age)

print(msg)