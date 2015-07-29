submission_ref = "ZYX9873"

case_data = '{ "dateReceived": "1993-11-01T12:00:00Z", "submissionRef": "' + submission_ref + '", "keyNumber": "KEY3243", "amountPaid": "12000", "lender": "GE Money Home Finance Limited", "mortgageDate": "1993-08-13T12:00:00Z", "titleNumber": "DN503122", "borrower": "", "propertyDetails": "", "emdref": ""}'

case1 = {
            "amountPaid": "100,000",
            "applicationReference": "T473LWW",
            "borrower": "Gregory Mann",
            "dateReceived": "2015-04-04T12:00:00Z",
            "emdref": "MD500",
            "keyNumber": "1122334",
            "lender": "Barry's Bank",
            "mortgageDate": "2015-04-01T12:00:00Z",
            "propertyDetails": "12 Hillview Road, Plymouth PL2 2QS",
            "submissionRef": "CSAM",
            "titleNumber": "DN503122"
        }

case2 = {
    "amountPaid": "200,000",
    "applicationReference": "U473LWW",
    "borrower": "Olivia Peck",
    "dateReceived": "2015-04-20T12:00:00Z",
    "emdref": "MD501",
    "keyNumber": "5566778",
    "lender": "Gary's Bank",
    "mortgageDate": "2015-04-07T12:00:00Z",
    "propertyDetails": "12 Hillview Road, Plymouth PL2 2QS",
    "submissionRef": "CSAM",
    "titleNumber": "DN503122"
}

stubcase = {"case" : case1}


stubcaselist = {"cases" : [case1, case2]}

daylist_adapter_response = { "abr" : "K123ABC" }

validate_title_response = { "validation_result" : "1" }