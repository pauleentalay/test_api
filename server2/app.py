from flask import Flask, request
from flask_restful import Resource, Api
import logging
import requests

# trial use of flask-restful

logging.basicConfig(filename='logs_server2.txt', encoding='utf-8', level=logging.INFO)

app = Flask(__name__)
api = Api(app)

#data = {"val": 10, "max_val": 13}

class Items(Resource):
    def post(self):
        reply = []
        data = request.json
        logging.info(f'data received = {data}, {type(data)}')
        data["val"] = data["val"] + 1
        if data["val"] < data["max_val"]:
            logging.info(f'but I am sending = {data}')
            request_con = requests.post("http://127.0.0.1:5000", json=data)         # requests from server1
            reply.append(data)
            return reply
        else:
            # trigger to start closing connections
            logging.info(f'this is the final form = {data}')
            reply.append(data)
            # no return here because we did not request here

api.add_resource(Items, '/')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003, debug=True)