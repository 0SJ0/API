import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import requests
import urllib.request as urllib2
app = Flask(__name__)

#Chargement Modèle
#target_url= 'https://scoring-credit.s3.eu-west-3.amazonaws.com/model.sav'
#filename = urllib2.urlopen(target_url)

#model = pickle.load(open('model.pkl', 'rb'))
print(pickle.load)

a=0

try :
    test_model=pickle.load(open('model.pkl', rb))
    a=0
except : 
    print(pickle.load)
    a=1

#Chargement dataset

target_url="https://scoring-credit.s3.eu-west-3.amazonaws.com/df_Xvalidation.txt"
data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
df = pd.read_csv(data, sep=',',index_col=0)
df=df.reset_index(drop=True)
df=df.iloc[:,0:]


@app.route('/')
def index():
    if(a==1) :
        return 'No hello, world'
    else :
        return 'No hello, world'
