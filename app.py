# imports
import flask
import pandas as pd




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


# if __name__ == '__main__':
#     delete_table()
#     initialize_db()
