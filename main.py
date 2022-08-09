import numpy as np
from flask import Flask, request, jsonify
import pandas as pd
import requests
import urllib.request as urllib2
import pickle
import sklearn

app = Flask(__name__)

#Chargement Modèle
#target_url= 'https://scoring-credit.s3.eu-west-3.amazonaws.com/model.sav'
#filename = urllib2.urlopen(target_url)

#model = pickle.load(open('model.pkl', 'rb'))
a=1


try :
    target_url="https://scoring-credit.s3.eu-west-3.amazonaws.com/model.sav"
    fichier= urllib2.urlopen(target_url)
    model = pd.read_pickle(fichier)
    a=1
except : 
    print(pickle.load)
    a=0




#Chargement dataset
target_url="https://scoring-credit.s3.eu-west-3.amazonaws.com/df_Xvalidation.txt"
data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
df = pd.read_csv(data, sep=',',index_col=0)
df=df.reset_index(drop=True)
df=df.iloc[:,0:]


@app.route('/')
def index():
    if(a==1) :
        return 'YES WORK'
    else :
        return 'NO WORK'
