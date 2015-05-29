import json

from application import app
from .utils import get_reference

from flask import request, Response

@app.route('/', methods=["GET"])
def index():
    return 'Cases API'

@app.route('/cases', methods=["GET","POST"])
def getCases():
    if request.method == 'GET':
        json_data=open('application/static/data/cases.json')
        data = json.load(json_data)
        return json.dumps(data)
    else: #POST will trigger this leg
        #Get case information from POST body
        case_data = request.get_json()

        #Get current case list
        jsonFile=open('application/static/data/cases.json')
        case_list = json.load(jsonFile)

        applicationReference = get_reference()

        #Create a new case from the case_data received
        case = {}
        case["titleNumber"] = case_data["titleNumber"]
        case["applicationReference"] = applicationReference
        case["dateReceived"] = case_data["dateReceived"]
        case["mortgageDate"] = case_data["mortgageDate"]
        case["lender"] = case_data["lender"]

        case_list["cases"].append(case)

        jsonFile=open('application/static/data/cases.json', "w")
        jsonFile.write(json.dumps(case_list, sort_keys=True, indent=4, separators=(',', ': ')))

        #Build response
        resp = Response('{"applicationReference" : "' + case["applicationReference"]+ '"}', status=200, mimetype='application/json')

        return resp


@app.route('/cases/<caseid>', methods=["GET"])
def getCase(caseid):
    json_data=open('application/static/data/' + caseid + '.json')
    data = json.load(json_data)
    return json.dumps(data)
