# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 19:02:35 2021

@author: Pepe

Celery is an asynchronous task queue. 
The general idea is that any resource consuming tasks that 
your application may need to run can be offloaded to the task queue, 
leaving your application free to respond to client requests.

A Celery installation has three core components:

    1. The Celery client. This is used to issue background jobs. 
    When working with Flask, the client runs with the Flask application.
    
    2. The Celery workers. These are the processes that run the 
    background jobs. Celery supports local and remote workers, 
    so you can start with a single worker running on the same 
    machine as the Flask server, and later add more workers as 
    the needs of your application grow.
    
    3. The message broker. The client communicates with the 
    the workers through a message queue, and Celery supports 
    several ways to implement these queues. The most commonly 
    used brokers are RabbitMQ and Redis.
"""

from flask import Flask
from celery import Celery

app = Flask(__name__)
#This URL tells Celery where the broker service is running.
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
#The CELERY_RESULT_BACKEND option is only necessary if you need to have 
#Celery store status and results from tasks.
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
