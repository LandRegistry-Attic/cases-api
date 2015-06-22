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

