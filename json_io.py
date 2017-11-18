from flask import Response
from flask import Flask
import json 

app = Flask(__name__)


@app.route('/readdata/<country>', methods = ['GET'])
def api_hello(country):
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(country + js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

if __name__ == "__main__":
	app.run()


