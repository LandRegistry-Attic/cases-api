Given(/^that a new case has been submitted$/) do

  #call submit_new_case function to create new case data
  $case_info = { "dateReceived" => "2020-11-01T12:00:00Z", "lender" => "Example Lender", "mortgageDate" => "2010-08-13T12:00:00Z", "titleNumber" => "DN1", "submissionRef" => "CSAM", "keyNumber" => "2244095", "amountPaid" => "200,000", "borrower" => "Cazza", "propertyDetails" => "12 Hillview Road, Plymouth PL2 2QS",  "emdref" => "MD501" }

  puts $case_info

  $new_case = submit_new_case($case_info)

end

Given(/^a unique reference is generated$/) do
  if $new_case["applicationReference"].nil?
    raise "No generated reference found"
  end
  if $new_case["applicationReference"]==""
    raise "Empty generated reference found"
  end
end

When(/^I view the daylist$/) do
  pending # Write code here that turns the phrase above into concrete actions
end

Then(/^I see the new case on the daylist$/) do
  pending # Write code here that turns the phrase above into concrete actions
end

Then(/^the cases are ordered by date and time$/) do
  pending # Write code here that turns the phrase above into concrete actions


end
