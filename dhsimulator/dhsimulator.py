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
import numpy as np
import queue
import os
import sys

'''initiallize flask'''
app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

'''Basic logging initializations'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Jesus Franco")

'''Some global variables that are needed'''
busy = False
q = queue.Queue()
t = ""
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
            crowdednessvar = .2
        if (time > 8) and (time <= 9.125):
            crowdednessvar = .5
        if (time > 9.125) and (time <= 11):
            crowdednessvar = 1
        if (time > 11) and (time <= 14):
            crowdednessvar = 3
        if (time > 14) and (time<=15.125):
            crowdednessvar = 1
        if (time > 15.125) and (time <= 17):
            crowdednessvar = .4
        if (time > 17) and (time <= 18):
            crowdednessvar = 2
        if (time > 18) and (time <=20):
            crowdednessvar = 1
        if (time > 20) and (time <=21):
            crowdednessvar = .8
    #rand= expo(crowdednessvar)
    make_noise(crowdednessvar)
    rand = main_dish_simulator()
    return render_template('bay.html', rand=rand)


'''asume exponential service time'''
def expo(Lambda):
    y = uniform()
    fx = -1*(np.log(1-y)/Lambda)
    return fx

'''Make threads'''
def make_noise(probability):
    if q.empty() == False:
        for i in range(q.qsize()):
            q.get()
    modifiedprobability = probability/100.00
    people = int(16000 * modifiedprobability)
    eat = []
    for i in  range(people):
        t = threading.Thread(target=main_dish_simulator)
        t.start()
        eat.append(t)
    for w in eat:
        w.join()
        #q.join()

'''time server takes is independent of the ammount of people'''
def main_dish_simulator():
    logger.info("Main thread name = {}".format(threading.current_thread().name))
    global busy
    if busy == True:
        q.put(t)
    elif busy == False:
        busy = True
        servicetime = expo(5)
        if q.get(t) == Empty:
            time.sleep(servicetime)
            busy = False
        else:
            q.get(t)
            q.join()
            time.sleep(servicetime)
            busy = False
    #q.join()
    return q.qsize()
