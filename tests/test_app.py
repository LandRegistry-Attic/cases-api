import unittest
import json

from application import app

case_data = '{ "dateReceived": "1993-11-01T12:00:00Z", "lender": "GE Money Home Finance Limited", "mortgageDate": "1993-08-13T12:00:00Z", "titleNumber": "DN9"}'

class TestCaseAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def test_case_list(self):
        response = self.app.get('/cases')
        response_json = json.loads(response.data.decode())
        cases = response_json['cases']
        assert len(cases) > 1
        assert cases[0]['titleNumber'] == 'DN1'


    def test_single_case(self):
        response = self.app.get('/cases/LR0101')
        response_json = json.loads(response.data.decode())
        case = response_json['case']
        assert case['titleNumber'] == 'DN1'
        assert case['entries'][0]['type'] == 'charge'

    def test_add_new_case(self):
        response = self.app.post('/cases', data=case_data, headers={"Content-Type":"application/json"})
        assert response.status_code == 200
