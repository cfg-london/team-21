from flask import Flask
from flask import Response
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/readdata/<country>/<age>/<year>/<index>",methods=['GET'])
def readdata(country,age,year,index):
    data = country
    return data


if __name__ == "__main__":
	app.run() 
