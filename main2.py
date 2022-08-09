import numpy as np
from flask import Flask, request, jsonify
import urllib.request as urllib2
import pickle



#Chargement Modèle
#target_url= 'https://scoring-credit.s3.eu-west-3.amazonaws.com/model.sav'
#filename = urllib2.urlopen(target_url)

#model = pickle.load(open('model.pkl', 'rb'))
a=1


target_url="https://scoring-credit.s3.eu-west-3.amazonaws.com/model.sav"
fichier= urllib2.urlopen(target_url)
model = pd.read_pickle(fichier)
a=1


app = Flask(__name__)


@app.route('/')
def index():
    if(a==1) :
        return 'YES WORK'
    else :
        return 'NO NO WORK'
