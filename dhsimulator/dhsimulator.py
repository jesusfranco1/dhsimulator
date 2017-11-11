import flask
from flask import Flask, Response, render_template, request, redirect, flash, url_for
from flaskext.mysql import MySQL
from numpy.random import uniform
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
@app.route('/baystate', methods=['GET', 'POST'])
def simulate():
    crowdednessvar = 0
    day = request.form.get("day")
    time = int(request.form.get("time"))
    if (day == "Tuesday" or day == "Thursday"):
        if (time <= 8) or (time >= 19):
            crowdednessvar = 10
        if (time > 8) and (time <= 9.125):
            crowdednessvar = 15
        if (time > 9.125) and (time <= 11):
            crowdednessvar = 19
        if (time > 11) and (time <= 14):
            crowdednessvar = 80
        if (time > 14) and (time<=15.125):
            crowdednessvar = 25
        if (time > 15.125) and (time <= 17):
            crowdednessvar = 10
        if (time > 17) and (time <= 18):
            crowdednessvar = 50
        if (time > 18) and (time <=20):
            crowdednessvar = 70
        else:
            crowdednessvar = 15

    rand = expo(5)
    #rand = BayDh
    return render_template('bay.html', rand=rand)
'''asume exponential service time'''
def expo(Lambda):
    y = uniform()
    fx = -1*(np.log(1-y)/Lambda)
    return fx
def main_dish_simulator():
