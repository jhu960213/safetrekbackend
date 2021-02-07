from pymongo import *
import pandas as pd
import json
from sqlalchemy import create_engine
from settings import *
import psycopg2

# connecting to postgrl database
db = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                      password=DB_PASSWORD, host=DB_HOST)
cursor = db.cursor()

# setting up env variables, paths, and database URI
table_name = "exposure"
data_base_URI = "postgres://lprwvaeypufzlm:e3fe0d7b99ad1b140f38f9c6165135551d1ce1da70245ddc78389e901c6cd77e@ec2-54-211-77-238.compute-1.amazonaws.com:5432/d31aa5atdorsnu"


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


# local storage class probably wont be used
class MyMongoDB(object):

    def __init__(self, db_name=None, table_name=None):
        # data base name and my table names that comes in
        self.db_name = db_name
        self.table_name = table_name

        # defining a mongo db client session object
        self.client = MongoClient("localhost", port=27017)

        # creating the data base that contains the set of tables
        self.DB = self.client[self.db_name]
        self.tables = self.DB[self.table_name]

    # inserts into our database table
    def insert_data(self, path=None):
        df = pd.read_csv(path)
        data = df.to_dict('records')
        self.tables.insert_many(data, ordered=False)
        print(f"All data has been exported to Mongo DB")


if __name__ == '__main__':
    delete_table()
    initialize_db()
