from flask import Flask, request
from flask_restful import Resource, Api
import json
import logging
import requests

logging.basicConfig(filename='logs_server1.txt', encoding='utf-8', level=logging.INFO)

app = Flask(__name__)

open("logs_server1.txt", "w").close()          #clear at the beginning

@app.route("/", methods=["POST"])
def post_response():
    #if request.method=="POST":
    data = request.json             
    logging.info(f'data received = {data}')
    data["val"] = data["val"] + 1
    logging.info(f'but I am sending = {data}')
    if data["val"] < data["max_val"]:
        request_con = requests.post("http://127.0.0.1:5003", json=data)     # requests from server2
        return display()
    else:
        # only trigger to start closing connections
        logging.info(f'No, I did not send. This is the final form = {data}')
        # no return here because we did not request here?

@app.route("/display", methods=["GET"])
def display():
    with open("logs_server1.txt") as f:
        f.seek(0)                               #place cursor in the beginning
        data = f.read()                         #read at 0
    open("logs_server1.txt", "w").close()       #clear after reading
    return data

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)