import json

from application import app
from .utils import add_to_daylist

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
        title_number = case_data["titleNumber"]

        ##title_validation_code = validate_title(title_number)
        ##if title_validation_code == 1:

        application_reference = add_to_daylist(title_number)

        #Get current case list
        jsonFile=open('application/static/data/cases.json')
        case_list = json.load(jsonFile)

        #Create a new case from the case_data received
        case = {}
        case["titleNumber"] = title_number
        case["applicationReference"] = application_reference
        case["dateReceived"] = case_data["dateReceived"]
        case["mortgageDate"] = case_data["mortgageDate"]
        case["lender"] = case_data["lender"]
        case["submissionRef"] = case_data["submissionRef"]
        case["keyNumber"] = case_data["keyNumber"]
        case["amountPaid"] = case_data["amountPaid"]
        case["borrower"] = case_data["borrower"]
        case["propertyDetails"] = case_data["propertyDetails"]
        case["emdref"] = case_data["emdref"]

        case_list["cases"].append(case)

        jsonFile=open('application/static/data/cases.json', "w")
        jsonFile.write(json.dumps(case_list, sort_keys=True, indent=4, separators=(',', ': ')))

        #Build response
        resp = Response('{"submissionRef" : "' + case["submissionRef"]+ '", "applicationReference" : "' + case["applicationReference"]+ '"}', status=200, mimetype='application/json')

        ##else:
        ##    resp = "title invalid"

        return resp


@app.route('/cases/<caseid>', methods=["GET"])
def getCase(caseid):
    json_data=open('application/static/data/' + caseid + '.json')
    data = json.load(json_data)
    return json.dumps(data)

def validate_title(title_number):
    return 1