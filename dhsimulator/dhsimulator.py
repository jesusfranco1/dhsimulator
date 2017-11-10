import flask
from flask import Flask, Response, render_template, request, redirect, flash, url_for
#from .dhsimulator import app
from flaskext.mysql import MySQL
import os, base64, datetime
import flask_login
from flask_login import current_user
import time

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

'''The first part of the program. Just the page that the user sees when he
   desires to use the simulator.
'''
@app.route('/')
def idle():
    return render_template('index.html')
