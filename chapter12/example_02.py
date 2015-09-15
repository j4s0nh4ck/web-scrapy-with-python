from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='/root/phantomjs/bin/phantomjs')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())
