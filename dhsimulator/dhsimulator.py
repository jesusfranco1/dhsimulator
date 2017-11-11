import flask
from flask import Flask, Response, render_template, request, redirect, flash, url_for
from flaskext.mysql import MySQL
import os, base64, datetime
import flask_login
from flask_login import current_user
import time
import random
import logging
import threading

'''initiallize flask'''
app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

'''Basic logging initializations'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Jesus Franco")

'''The first part of the program. Just the page that the user sees when he
   desires to use the simulator.
'''
@app.route('/')
def idle():
    return render_template('index.html')

'''User decides to simulate bay state dinning hall'''
@app.route('/baystate')
def simulate():
    rand = random.randint(0,10)
    return render_template('bay.html', rand=rand)

'''Simulate Bay State Dinning Hall. The threads simulate the users.
   I am trying to use statistics so that the user can determine when
   it is usually the best time to go to the dinning hall. By best,
   I mean the least amount of people for both breakfast times, lunch
   times, and dinner times.
'''
class BayDh(threading.Thread):
    '''Constructor for class'''
    def __init__():
        self.hashfn = hashfn
        self.count = count
        self.message = random.choice(string.ascii_uppercase)
        super(BayDh, self).__init__()
    def run(self):
        return 0
    '''simulate work/ wait time for the main dish stand'''
    def simulate_main_dish(count):
        return 0
