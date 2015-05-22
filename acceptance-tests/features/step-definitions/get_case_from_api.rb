Given(/^that a case is lodged$/) do
  $posted_data_hash = post_case()
end

When(/^I give a valid get request$/) do
  $retreived_case_json = get_a_case($posted_data_hash["applicationReference"])
end

Then(/^the case details are returned$/) do
  $retreived_case_json != $posted_data_hash.to_json
end
