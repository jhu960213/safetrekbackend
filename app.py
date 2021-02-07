# imports
import flask
from flask import request
import pandas as pd

path = "./covid.csv"
exposure = pd.read_csv(path)  # with the default column names

# flask object
app = flask.Flask(__name__)


#
# backend API methods to interact with our datasbase
#

# flask api routing methods
@app.route('/', methods=['GET'])
def query_by_long_lat():
    tempDict = {}
    try:
        lat = float(request.args.get('lat'))
        long = float(request.args.get('long'))

        # storing the sum of abs diff of lat and long and its index value
        for i in range(0, exposure.shape[0]):
            cur_lat = exposure.iloc[i, 2]
            cur_long = exposure.iloc[i, 3]
            tempDict[abs(cur_lat-lat) + abs(cur_long-long)] = i

        # find the min key
        minKey = min(tempDict.keys())

        # extract desired row from dataframe
        extracted_row = exposure.iloc[tempDict[minKey], :]
        return flask.jsonify(extracted_row)
    except Exception as e:
        print(e)
        return f'Invalid processing!'


if __name__ == '__main__':
    app.run()
