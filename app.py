# imports
import flask
import psycopg2
from database import *
from settings import *
import pandas as pd
from sqlalchemy import create_engine

# setting up env variables, paths, and database URI
table_name = "exposure"
path = "./covid.csv"
data_base_URI = "postgres://lprwvaeypufzlm:e3fe0d7b99ad1b140f38f9c6165135551d1ce1da70245ddc78389e901c6cd77e@ec2-54-211-77-238.compute-1.amazonaws.com:5432/d31aa5atdorsnu"
myData = pd.read_csv(path)  # with the default column names

# flask app
my_server = flask.Flask(__name__)

# connecting to postgrl database
db = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                      password=DB_PASSWORD, host=DB_HOST)
cursor = db.cursor()

# delete desired table in postgres
def delete_table():
    try:
        cursor.execute("DROP TABLE %s;" % table_name)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print(e + "Skipping delete operation!")




# initialize database with records
def initialize_db():
    try:
        engine = create_engine(data_base_URI)
        myData.to_sql(table_name, engine)
    except Exception as e:
        if str(e) == f"Table '{table_name}' already exists.":
            print("***Table already exists! Skipping table creation.***")


#
# backend API methods to interact with our datasbase
#

# flask api routing methods
@my_server.route('/', methods=['GET'])
def home():
    # cursor.execute("SELECT * FROM %s;" % table_name)
    return "Hello, world"


# if __name__ == '__main__':
#     delete_table()
#     initialize_db()
