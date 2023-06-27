#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#set as headless (no GUI)
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode

#store the firefox webdriver object inside variable 'browser'
browser = webdriver.Firefox(options=opts)

#from object 'browser' access method 'get' with parameter 'url' to open the web address
browser.get("https://duckduckgo.com")

#find element using xpath and sent search term
search = browser.find_element_by_xpath("//*[@id='search_form_input_homepage']")
search.send_keys("Selenium" + Keys.RETURN)

#quit the browser
browser.quit()


