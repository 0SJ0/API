import numpy as np
from flask import Flask, request, jsonify
import pandas as pd
import requests
import urllib.request as urllib2
import pickle



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

app = Flask(__name__)


@app.route('/')
def index():
    if(a==1) :
        return 'YES WORK'
    else :
        return 'NO NO WORK'
    
@app.route('/ID')
def ID():
    return 'ID du client'

@app.route('/ID/<id>', methods=['GET'])
def Prediction(id):
    ID=int(id) #100194
    index=df[df["SK_ID_CURR"]==ID].index.values[0] #102616
    proba=index
    #proba=model.predict_proba(df.iloc[index:index+1,:])[0][1]
    return jsonify({'proba' : proba})



if __name__ == '__main__':
    app.run()
