import numpy as np
from flask import Flask, request, jsonify
import pickle
import requests
import urllib.request as urllib2


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello, world'