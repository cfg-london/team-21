from flask import Flask
from flask import Response
from flask_cors import cross_origin
import json
import getSingleValue
import indicatorMap
import multiVariate

app = Flask(__name__)

@app.route("/line_graph")
def hello1():
    return render_template('./_includes/head.html',
                           'header.html',
                           './_includes/footer.html')

@app.route("/complex_graph")
def hello2():
    return render_template('./_includes/head.html',
                           'graph.html',
                           './_includes/footer.html')


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

@app.route("/possibleyears/<country>/<index>",methods=['GET'])
@cross_origin()
def possibleyears(country,index):
    indicator = indicatorMap.dict_map[index]
    years = getSingleValue.possibleyear(indicator,country)
    data = json.dumps(years)
    print(data)
    resp = Response( data,status=200,mimetype='application/json')
    return resp

@app.route("/possiblegroups/<country>/<index>/<year>",methods=['GET'])
@cross_origin()
def possiblegroups(country,index,year):
    indicator = indicatorMap.dict_map[index]
    groups = getSingleValue.possiblegroup(indicator,country,year)
    data = json.dumps(groups)
    print(data)
    resp = Response(data,status=200,mimetype='application/json')
    return resp

@app.route("/oneCountryOverTime/<index>/<country>/<age>",methods=['GET'])
@cross_origin()
def oneCountryOverTime(index,country,age):
    indicator = indicatorMap.dict_map[index]
    dataOverYears = multiVariate.one_country_over_time(indicator,country,age)
    data = json.dumps(dataOverYears)
    resp = Response(data,status=200,mimetype='application/json')
    return resp

#@app.route("/oneCountryOverTime/<index>/<country>",methods=['GET'])
#@cross_origin()
#def allAgesGroups(index,country):
#    indicator = indicatorMap.dict_map[index]
#    ageGroups=
#    for (group in ageGroups):


@app.route("/compareCountry/<index>/<year>/<age>",methods=['GET'])
@cross_origin()
def compareCountry(index,year,age):
    indicator = indicatorMap.dict_map[index]
    countryValues = getSingleValue.compareCountry(indicator, year, age)
    data = json.dumps(countryValues)
    resp = Response(data,status=200,mimetype='application/json')
    return resp

@app.route("/compareAgeGroups/<index>/<country>/<year>",methods=['GET'])
@cross_origin()
def compareAgeGroups(index,country,year):
    indicator = indicatorMap.dict_map[index]
    ageValues = getSingleValue.comparegroup(indicator, country, year)
    data = json.dumps(ageValues)
    resp = Response(data,status=200,mimetype='application/json')
    return resp

if __name__ == "__main__":
	app.run() 
