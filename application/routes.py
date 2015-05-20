import json

from application import app

@app.route('/', methods=["GET"])
def index():
    return 'Cases API'

@app.route('/cases', methods=["GET"])
def cases():
    json_data=open('application/static/data/cases.json', "r")
    data = json.load(json_data)
    return json.dumps(data)
