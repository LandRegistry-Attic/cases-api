import os

def get_reference():
    with open('application/static/data/reference.txt',"r+") as file:
        ref_number = file.read()
        ref_int = int(ref_number) + 1
        ref_number = str(ref_int)
        file.seek(0)
        file.write(ref_number)

    reference = "AB" + ref_number

    return reference