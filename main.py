from database import MyMongoDB

path = "./covid.csv"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myDataBase = MyMongoDB(db_name='MyCovidDataSet', table_name='Exposure')
    myDataBase.insert_data(path)


