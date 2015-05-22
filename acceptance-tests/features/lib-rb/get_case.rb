def get_a_case(app_ref)
  uri = URI.parse($CASES_API_DOMAIN)
  http = Net::HTTP.new(uri.host, uri.port)
  request = Net::HTTP::Get.new('/cases/' + app_ref,  initheader = {'Content-Type' =>'application/json'})
  request.basic_auth $http_auth_name, $http_auth_password
  response = http.request(request)
  if (response.code != '200') then
    raise "Unable to retrieve case with application ref " + app_ref
  end
  return response.body
end
