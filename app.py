import flask
from flask import request
import pandas as pd

path = "./covid.csv"
myData = pd.read_csv(path)  # with the default column names

# flask app
my_server = flask.Flask(__name__)


#
# safetrek backend API methods to interact with our datasbase
#

# flask api routing methods
@my_server.route('/', methods=['GET'])
def home():
    return "Hello, safetrek home!"
