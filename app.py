# imports
import flask
from flask import request
import pandas as pd
from flask_cors import CORS, cross_origin

path = "./covid.csv"
exposure = pd.read_csv(path)  # with the default column names

# flask object
app = flask.Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": "https://safetrekbackend.herokuapp.com/"}})


#
# backend API methods to interact with our datasbase
#

# flask api routing methods
@app.route('/', methods=['GET'])
@cross_origin(origin="https://safetrekbackend.herokuapp.com/", headers=['Content- Type', 'Authorization'])
def find_risk():
    tempDict = {}
    num_nearby_locations = 3
    try:
        lat = float(request.args['lat'])
        long = float(request.args['long'])

        # storing the sum of abs diff of lat and long and its index value
        for i in range(0, exposure.shape[0]):
            cur_lat = exposure.iloc[i, 2]
            cur_long = exposure.iloc[i, 3]
            tempDict[(abs(cur_lat - lat) ** 2 + abs(cur_long - long) ** 2) ** (1 / 2)] = i

        # get a list of the sorted keys
        keys = list(tempDict.keys())
        keys.sort()

        # getting the smallest 3 distances from the inputed long and lat
        min0 = keys[0]
        min1 = keys[1]
        min2 = keys[2]

        # extract the 3 closest locations
        loc0 = exposure.iloc[tempDict[min0], :]
        loc1 = exposure.iloc[tempDict[min1], :]
        loc2 = exposure.iloc[tempDict[min2], :]
        # print(loc0)
        # print(loc1)
        # print(loc2)

        # define risk values for each location
        risk0 = loc0[-1] + loc0[5]
        risk1 = loc1[-1] + loc1[5]
        risk2 = loc2[-1] + loc2[5]

        # weighted average risk
        weight_avg_risk = (risk0 * min0 + risk1 * min1 + risk2 * min2) / num_nearby_locations

        # return a json key value pair
        response = flask.jsonify({'weighted_avg_risk': weight_avg_risk})
        return response

    except Exception as e:
        print(e)
        return f'Invalid processing happened on the backend!'


if __name__ == '__main__':
    app.run()
