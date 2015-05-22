def post_case()
  case1 = '{
  "case": {
      "titleNumber": "DT91660",
      "applicationReference": "NB586",
      "dateReceived": "2007-10-08T12:00:00Z",
      "entries": [
          {
              "type": "charge",
              "date": "2007-08-13T12:00:00Z",
              "text": "REGISTERED CHARGE dated 13 August 2007."
          },
          {
              "type": "charge proprietor",
              "date": "2007-08-13T12:00:00Z",
              "text": "Proprietor: GE Money Home Finance Limited (Co. Regn. No. 592986) of Building 4, Hatters Lane, Croxley Green Business Park, Watford WD18 8YF."
          }
      ],
      "mortgageDate": "2007-08-13T12:00:00Z",
      "lender": "GE Money Home Finance Limited"
  }
}'
  case_hash = JSON.parse(case1)

  return case_hash["case"]
end
