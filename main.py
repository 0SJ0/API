import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import requests
#import urllib.request as urllib2
app = Flask(__name__)

#Chargement Modèle
#filename = 'Data/model.sav'
#model = pickle.load(open(filename, 'rb'))


@app.route('/')
def index():
    return 'hello, world'
