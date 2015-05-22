After do | scenario |
  if (scenario.failed?)
      page.save_screenshot "sshot-#{Time.new.to_i}.png"
  end
end
