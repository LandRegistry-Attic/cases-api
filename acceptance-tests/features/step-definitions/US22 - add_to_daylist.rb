Given(/^I have case information$/) do

  @case_info = {"dateReceived" => "2020-11-01T12:00:00Z",
                "lender" => "Example Lender",
                "mortgageDate" => "2010-08-13T12:00:00Z",
                "titleNumber" => "DN503122",
                "submissionRef" => "CSAM",
                "keyNumber" => "2244095",
                "amountPaid" => "200,000",
                "borrower" => "Cazza",
                "propertyDetails" => "12 Hillview Road, Plymouth PL2 2QS",
                "emdref" => "MD501"
               }
end

When(/^a case is submitted$/) do
  #Call submit_new_case function to pass '@case_info' to the CASES_API
  @cases_api_response = submit_new_case(@case_info)
  puts @cases_api_response
end

Then(/^an ABR is returned$/) do
    abr = cases_api_response["applicationReference"]
  if abr.length != 7 then
    raise "abr not 7 characters. Abr is #{abr}"
  end
end

Given(/^it consists of a closed title number$/) do
  #make it a closed title
  @case_info["titleNumber" => "BK506696"]
end

Then(/^a title closed message is returned$/) do
  pending # Write code here that turns the phrase above into concrete actions
end
