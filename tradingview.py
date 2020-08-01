#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



#set as headless (no GUI)
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode

#store the firefox webdriver object inside variable 'browser'
browser = webdriver.Firefox()

#from object 'browser' access method 'get' with parameter 'url' to open the web address
browser.get('https://www.tradingview.com/screener/')

#find element using xpath
search = browser.find_element_by_xpath('//*[@id="js-screener-container"]/div[2]/div[13]')

element = '//*[@id="js-screener-container"]/div[2]/div[13]'

#implement wait for 3s
WebDriverWait(browser, timeout=30).until(expected_conditions.element_to_be_clickable((By.XPATH, element)))

#click the element
search.click()