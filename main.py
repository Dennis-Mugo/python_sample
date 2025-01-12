from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random


app = Flask(__name__)
CORS(app)

response_format = {
    "data": {},
    "errors": [],
    "status": 200
}






def hello():
    res = response_format.copy()
    res["data"] = {"hello": "world"}
    return jsonify(res)

    
    


app.add_url_rule("/", "hello", hello, methods=["GET"])



if __name__=='__main__':
    app.run(host="127.0.0.1", port=3000, debug=True)