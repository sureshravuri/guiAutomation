from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import logging
time.sleep(5)
logFileMode='w'
logFormat = '%(asctime)s %(levelname)-8s %(message)s'
logDateFmt='%d %b %H:%M:%S'
logfile = '/Users/suresh/Desktop/guiproject/logging/logfile.log'
logLevel = logging.INFO
logging.basicConfig(level=logLevel, format=logFormat, datefmt=logDateFmt, filename=logfile, filemode=logFileMode)
driver = webdriver.Firefox()
username = 'chetanx.bharadwaj@intel.com'
password = 'Mcafee123'
loginbutton = 'btnLogin'
url = 'https://home.mcafee.com/Store/Promo.aspx?id=logout'
login = ".//*[@id='ctl00_m_HeaderFullNavigation_ucDashBoardPersonalNav_PersonalNavigation']/li[3]/a"

class TestCase():
    
    def urlLaunch(self,url):
        try:
            driver.get(url)
            driver.implicitly_wait(45)
        except Exception as er:
            return False
            print "Not able to launch URL"
    def login(self,login,username,password,button):
        try:
            driver.implicitly_wait(25)
            driver.find_element_by_xpath(login).click()
            driver.find_element_by_xpath(username).send_keys()
            driver.find_element_by_xpath(password).send_keys()
            driver.find_element_by_name(button).click()
        except Exception as er:
            return False
            print "Not able to login"
    def downloadbuild(self,downloadmacbuildbuttonid):
        timeout = 15
        try:
            Downloadbuttonpresent = EC.presence_of_element_located((By.ID, downloadmacbuildbuttonid))
            driver.find_element_by_id(downloadmacbuildbuttonid).click()
            WebDriverWait(driver, timeout).until(Downloadbuttonpresent)
        except TimeoutException:
            print "timeout"

    def waituntilelementload(elementtoload):
        timeout = 15
        try:
            Downloadbuttonpresent = EC.presence_of_element_located((By.XPATH, elementtoload))
            driver.find_element_by_id(elementtoload).click()
            WebDriverWait(driver, timeout).until(Downloadbuttonpresent)
        except TimeoutException:
            print "timeout"

if __name__ == "__main__":
    testcasobj = TestCase()
    testcasobj.urlLaunch(url)
    testcasobj.login(login,username,password,loginbutton)
    print login
    print username
    print password
    print loginbutton

