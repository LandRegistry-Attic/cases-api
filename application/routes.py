from application import app
from .utils import add_to_daylist, validate_title, get_worklist, get_case_details
from flask import request, Response

import json

@app.route('/', methods=["GET"])
def index():
    return 'Cases API'

@app.route('/cases', methods=["GET","POST"])
def getCases():
    if request.method == 'GET':
        # team_id currently hardcoded to 1578, a team with 6 cases on UACT, future story will exist to correctly ascertain this value
        team_id = '20007'
        data = get_worklist(team_id)
        #If the cases array is empty
        if not data["cases"]:
            return Response("No cases found for {0} for team".format(team_id), 404)
        else:
            return json.dumps(data)
    else: #POST will trigger this leg
        #Get case information from POST body
        case_data = request.get_json()
        title_number = case_data["titleNumber"]

        title_validation_code = validate_title(title_number)
        if title_validation_code == "1":

            application_reference = add_to_daylist(title_number)

        else:
            application_reference = ""

        resp = Response('{"submissionRef" : "' + case_data["submissionRef"] + '", "applicationReference" : "' + application_reference + '", "TitleValidationCode" : "' + title_validation_code + '"}', status=200, mimetype='application/json')
        return resp


@app.route('/cases/<caseid>', methods=["GET"])
def getCase(caseid):
    data = get_case_details(caseid)

    if data:
        return json.dumps(data)
    else:
        return Response("No case found for {0}".format(caseid), 404)
