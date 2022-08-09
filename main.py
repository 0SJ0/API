import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import urllib.request as urllib2
import requests

app = Flask(__name__)

#Chargement Modèle
#filename = 'Data/model.sav'
#model = pickle.load(open(filename, 'rb'))


@app.route('/')
def index():
    return 'hello, world'
