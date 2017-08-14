import sys
import os
import atomac.ldtp as ldtp
testcaseName = sys.argv[0][:-3]
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import constants
import commonFns
import logging
import time
from time import gmtime, strftime
testcaseDescription = "Build install from QA server"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#https://ftp.mozilla.org/pub/firefox/releases/45.0/mac/en-US/
class TestCase():

    def verify(self):
        driver = commonFns.getDriver()
        commonFns.Launchurl(constants.Data.get('url'),driver)
        commonFns.login(constants.Data.get('login'),driver,constants.Data.get('username'),
                        constants.Data.get('password'),constants.Data.get('loginbutton'))
        #commonFns.GetserialKey(driver,constants.Data.get('downloadmacbuildbuttonid'))
if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.verify()
