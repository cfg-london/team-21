from flask import Flask
from flask import Response
import json
import getSingleValue
import indicatorMap

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/readdata/<country>/<index>/<age>/<year>",methods=['GET'])
def readdata(country,age,year,index):
    indicator = indicatorMap.dict_map[index]
    data = json.dumps(getSingleValue.getvalue(indicator,courtry,year,age))
    return data


if __name__ == "__main__":
	app.run() 
