import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

#Chargement Modèle
filename = 'DATA/model.sav'
model = pickle.load(open(filename, 'rb'))


@app.route('/')
def index():
    return 'hello, world'
