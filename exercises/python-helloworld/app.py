from flask import Flask, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s, %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

@app.route("/")
def hello():
    logging.debug("/hello endpoint was reached")
    return "Hello World!"

@app.route("/status")
def status():
    logging.debug("/status endpoint was reached")
    response = {
        "result": "OK - healthy",
        "user": "admin"
    }
    return jsonify(response)

@app.route("/metrics")
def metrics():
    logging.debug("/metrics endpoint was reached")
    response = {
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        },
        "user" : "admin"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
