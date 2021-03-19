import flask
from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

currentTemp = 72
setTemp = 70

@app.route('/', methods=['GET'])
def home():
    return "<h1>CS 4047 Test Home Page</h1><p>This site is a prototype API for a therhmostat.</p>"


# A route to return all of the available entries in our catalog.
# #@app.route('/ThermsAreUs/api/v1.0/current-temp', methods=['GET'])
@app.route('/c', methods=['GET'])
def api_get_current_temp():
    return str(currentTemp)


# #@app.route('/ThermsAreUs/api/v1.0/current-temp', methods=['GET'])
@app.route('/s', methods=['GET'])
def api_get_set_temp():
    return str(setTemp)

# #@app.route('/ThermsAreUs/api/v1.0/current-temp', methods=['PUT', POST])
@app.route('/s', methods=['PUT'])
def api_put_set_temp():
    global setTemp
    setTemp = request.args.get('temp')
    return str(setTemp)

app.run(host='0.0.0.0')
