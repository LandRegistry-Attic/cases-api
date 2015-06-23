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
end

Then(/^an ABR is returned$/) do
    abr = @cases_api_response["applicationReference"]
  if abr.length != 7 then
    raise "abr not 7 characters. Abr is #{abr}"
  end
end

Given(/^the title number is invalid$/) do
  #make it an invalid format of title number
  @case_info["titleNumber"] = "DUFFNUM1"
end

Given(/^the title number does not exist$/) do
  #Make it a non existent title number
  @case_info["titleNumber"] = "DN12340"
end

Given(/^it consists of a closed title number$/) do
  #make it a closed title
  @case_info["titleNumber" => "BK506696"]
end

Given(/^the title number is closed and not continued$/) do
  pending # Write code here that turns the phrase above into concrete actions
end


Then(/^a Title validation code of 1 is returned$/) do
    validation_no = @cases_api_response["TitleValidationCode"]
    assert validation_no == "1"
end

Then(/^a Title validation code of 3 is returned$/) do
    validation_no = @cases_api_response["TitleValidationCode"]
    assert validation_no == "3"
end

Then(/^a Title validation code of 2 is returned$/) do
  validation_no = @cases_api_response["TitleValidationCode"]
  assert validation_no == "2"

end


Then(/^a title closed message is returned$/) do
  pending # Write code here that turns the phrase above into concrete actions
end
