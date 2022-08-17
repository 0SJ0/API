# Import libraries
import numpy 
from flask import Flask, request, jsonify
import gunicorn
import fsspec
import pickle
import pandas as pd
#import urllib.request as urllib2
#import requests

#S3 connexion
#Téléchargement data plus modèle
S3_connexion=0


try :
    df = pd.read_csv(
        f"s3://scoring-credit/df_Xvalidation.csv",
        storage_options={
            "key": "AKIARWSZ2E3CBMBY3SFF",
            "secret": "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",
        },index_col=0
    ).reset_index(drop=True)

    model = pd.read_pickle(
        f"s3://scoring-credit/model.sav",
        storage_options={
            "key": "AKIARWSZ2E3CBMBY3SFF",
            "secret": "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",
     }
    )
    S3_connexion=1
except :
    print("Erreur")
    S3_connexion=0


#Application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bienvenue sur le modèle de scoring'

@app.route('/ID')
def ID():
    return 'ID du client'

@app.route('/ID/<id>', methods=['GET'])
def Prediction(id):
    try :
        ID=int(id) #100194
        index=df[df["SK_ID_CURR"]==ID].index.values[0]
        score=round(model.predict_proba(df.iloc[index:index+1,:])[0][1]*100) #368305
        defaut_credit=0
        if (score>60) : defaut_credit=1
        return jsonify({'Score' : score, "Defaut_credit" : defaut_credit})
    except :
        return jsonify({"erreur" : S3_connexion})
    
    
   


if __name__ == '__main__':
    app.run()
    
    
#Fin
