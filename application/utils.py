import json
import requests

def add_to_daylist(title_number):
    #with open('application/static/data/reference.txt',"r+") as file:
    #    ref_number = file.read()
    #    ref_int = int(ref_number) + 1
    #    ref_number = str(ref_int)
    #    file.seek(0)
    #    file.write(ref_number)

    #reference = "AB" + ref_number

    response = requests.get('http://localhost:8888/' + title_number)
    data = response.json()
    reference = data["ABR"]

    return reference