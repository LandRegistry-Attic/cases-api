def get_a_case(app_ref)
  #breaks down URI into component parts
  uri = URI.parse($CASES_API_DOMAIN)
  #use libraries Net & HTTP to allocate specific host and port parts for the variable
  http = Net::HTTP.new(uri.host, uri.port)
  #creates the get request for specific app_ref, which will be in JSON format
  request = Net::HTTP::Get.new('/cases/' + app_ref,  initheader = {'Content-Type' =>'application/json'})
  #this bit isnt really required at the moment as no auth name or password set
  request.basic_auth $http_auth_name, $http_auth_password
  #combines the 2 parts http and request to get a response through the api
  response = http.request(request)
  # != means does not equal
  if (response.code != '200') then
    raise "Unable to retrieve case with application ref " + app_ref
  end
  return response.body
end
