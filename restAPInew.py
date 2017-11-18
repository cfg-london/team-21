from flask import Flask
from flask import Response
from flask_cors import cross_origin
import json
import getSingleValue
import indicatorMap

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/readdata/<country>/<index>/<age>/<year>",methods=['GET'])
@cross_origin()
def readdata(country,age,year,index):
    
    print( country )
    print( age )
    print( year )
    print( index )
    
    indicator = indicatorMap.dict_map[index]
    data = json.dumps(getSingleValue.getvalue(indicator,country,year,age))
    responseData = { 'data' : data }
    print(responseData)
    resp = Response( data,status=200,mimetype='application/json')
    
    return resp


if __name__ == "__main__":
	app.run() 