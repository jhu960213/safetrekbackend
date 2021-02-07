# imports
import flask
from settings import *
import psycopg2

# connecting to postgrl database
db = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                      password=DB_PASSWORD, host=DB_HOST)
cursor = db.cursor()

# flask app
app = flask.Flask(__name__)


#
# backend API methods to interact with our datasbase
#

# flask api routing methods
@app.route('/', methods=['GET'])
def home():
    # cursor.execute("SELECT * FROM %s;" % table_name)
    return "Hello, world"

