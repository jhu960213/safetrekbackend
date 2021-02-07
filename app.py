# imports
import flask
from flask import request
import pandas as pd

path = "./covid.csv"
myData = pd.read_csv(path)  # with the default column names

# flask app
app = flask.Flask(__name__)


#
# backend API methods to interact with our datasbase
#

# flask api routing methods
@app.route('/', methods=['GET'])
def query_all():
    try:
        return myData.to_json()
    except KeyError as e:
        return f'Invalid location!'
