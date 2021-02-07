# imports
import flask
from settings import *
from database import *


# flask app
app = flask.Flask(__name__)


#
# backend API methods to interact with our datasbase
#

# flask api routing methods
@app.route('/', methods=['GET'])
def home():
    cursor.execute("SELECT * FROM %s;" % table_name)
    return cursor.fetchall()

