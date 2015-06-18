#this function runs through all cases on caselist and matches data
def match_data_in_caselist_rows(caselist,case_details)
  match = false

  caselist.each do |row|
    if (row.text.include? case_details["titleNumber"]) and (row.text.include? case_details["applicationReference"]) and (row.text.include? case_details["dateReceived"])
    match = true
    end
  end
  return match
end

#formats the date and time in format 18 February 1997 12:00
def format_date_time(date_time)
  return DateTime.parse(date_time).strftime('%d %B %Y %I:%M')
end
