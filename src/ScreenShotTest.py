#!/usr/bin/python
import sys
import commands as c

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

URL = sys.argv[1]

Snapshot_Dir = '/home/ubuntu/webshot/website/public/snapshots/'
Snapshot_Dir_Public = 'snapshots/'

binary = FirefoxBinary('/usr/bin/firefox')

## Create a new instance of the Firefox driver
driver = webdriver.Firefox(firefox_binary = binary)

driver.implicitly_wait(5)

driver.get(URL)

driver.get_screenshot_as_file(Snapshot_Dir + 'snapshot.png')

driver.close()

#clear directory in tmp
cmd = 'rm -R /tmp/tmp*'
c.getoutput(cmd)

print Snapshot_Dir_Public + 'snapshot.png'

