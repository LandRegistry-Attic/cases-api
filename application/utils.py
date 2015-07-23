import json
import requests
import os

def add_to_daylist(title_number):
    response = requests.post('http://localhost:8888/DaylistAdapter/cases/' + title_number)
    data = response.json()
    reference = data["abr"]

    return reference

def validate_title(title_number):
    response = requests.get(os.getenv("TITLES_API_URL","http://localhost:5005/validate/") + title_number)
    data = response.json()
    validation_result = data["validation_result"]

    return str(validation_result)

def get_worklist(team_id):
    response = requests.get('http://localhost:8888/DaylistAdapter/cases/teamid/' + team_id)
    worklist = response.json()

    return str(worklist)

def get_case_details(abr):
    response = requests.get('http://localhost:8888/DaylistAdapter/case/' + abr)
    case_info = response.json()

    return case_info