import unittest
import json
import mock

from application import app
from application.utils import validate_title, add_to_daylist
from stubresponses import submission_ref, case_data, stubcase, stubcaselist, daylist_adapter_response, validate_title_response

class TestCaseAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/')
        assert response.status_code == 200

    @mock.patch('requests.get')
    @mock.patch('requests.Response')
    def test_case_list(self, mock_response, mock_get):
        mock_response.json.return_value = stubcaselist
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.app.get('/cases')
        response_json = json.loads(response.data.decode())
        cases = response_json['cases']
        assert len(cases) == 2
        assert cases[0]['titleNumber'] == 'DN503122'

    @mock.patch('requests.get')
    @mock.patch('requests.Response')
    def test_single_case(self, mock_response, mock_get):
        mock_response.json.return_value = stubcase
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.app.get('/cases/LR0101')
        response_json = json.loads(response.data.decode())
        case = response_json['case']
        assert case['titleNumber'] == 'DN503122'

    @mock.patch('requests.post')
    @mock.patch('requests.get')
    @mock.patch('requests.Response')
    @mock.patch('requests.Response')
    def test_add_new_case(self, mock_response1, mock_response2, mock_get, mock_post):
        app_ref = 'K123ABC'

        #mock the post to daylist adapter
        mock_response1.json.return_value = daylist_adapter_response
        mock_response1.status_code = 200
        mock_post.return_value = mock_response1

        #mock the get to titles api validate title
        mock_response2.json.return_value = validate_title_response
        mock_response2.status_code = 200
        mock_get.return_value = mock_response2

        response = self.app.post('/cases', data=case_data, headers={"Content-Type":"application/json"})
        response_json = json.loads(response.data.decode())

        app_ref_back = response_json['applicationReference']
        submission_ref_returned = response_json['submissionRef']

        assert response.status_code == 200
        assert app_ref_back == app_ref
        assert submission_ref == submission_ref_returned
