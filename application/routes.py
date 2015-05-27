import json

from application import app
from .utils import get_reference

@app.route('/', methods=["GET"])
def index():
    return 'Cases API'

@app.route('/cases', methods=["GET"])
def getCases():
    json_data=open('application/static/data/cases.json')
    data = json.load(json_data)
    return json.dumps(data)

@app.route('/cases/<caseid>', methods=["GET"])
def getCase(caseid):
    json_data=open('application/static/data/' + caseid + '.json')
    data = json.load(json_data)
    return json.dumps(data)
