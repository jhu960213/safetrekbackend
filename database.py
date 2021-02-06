from pymongo import *
import pandas as pd
import json


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




