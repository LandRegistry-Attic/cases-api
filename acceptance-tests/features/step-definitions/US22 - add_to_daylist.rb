Given(/^I have case information$/) do
  #call submit_new_case function to create new case data
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
  case_references = submit_new_case(@case_info)
  @abr = case_references["applicationReference"]
end

Then(/^an ABR is returned$/) do
  if @abr.length != 7 then
    raise "abr not 7 characters. Abr is #{@abr}"
  end
end
