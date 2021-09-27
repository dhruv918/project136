from flask import Flask, jsonify, request
from data import data
import csv 
movies=[]
with open('final.csv')as f:
    reader = csv.reader(f)
    data = list(reader)
    movies = data[1:]


app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":movies,
        "message": "success"
    }), 200

@app.route("/stars")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()