def submit_new_case(case_info)
  #CASES_API_DOMAIN has been populated previously in support/env.rb
  uri = URI.parse($CASES_API_DOMAIN)
  #use libraries Net & HTTP to allocate specific host and port parts for the variable
  http = Net::HTTP.new(uri.host, uri.port)
  #creates the Post request with specific case_info data, which will be in JSON format
  request = Net::HTTP::Post.new('/cases', initheader = {'Content-Type' =>'application/json'})
  # set up data and assign to request.body

  puts request

  request.body = case_info.to_json
  
  puts request.body
  request.basic_auth $http_auth_name, $http_auth_password
  #combines the 2 parts http and request to get a response through the api

  puts http.request(request)

  response = http.request(request)

  if (response.code != '200') then
    raise "Unable to submit a case"
  end
      parsed_response = JSON.parse(response.body)

  return parsed_response
end
