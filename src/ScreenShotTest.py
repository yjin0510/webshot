#!/usr/bin/python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

Snapshot_Dir = '/home/ubuntu/webshot/snapshot/'

binary = FirefoxBinary('/usr/bin/firefox')

## Create a new instance of the Firefox driver
driver = webdriver.Firefox(firefox_binary = binary)

#driver.implicitly_wait(10)

driver.get("http://www.google.com")

driver.get_screenshot_as_file(Snapshot_Dir + 'snapshot.png')

driver.close()


