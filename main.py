import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello, world'
