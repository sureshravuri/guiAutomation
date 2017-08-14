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
testcaseDescription = "consumer4.0 application Launching"

class TestCase():

    def verify(self,Appbundleid):
        if not commonFns.launchApplication(Appbundleid):
            logging.debug("Failed to launch consumer4.0")
        '''print '############'
            filename = testcaseDescription + "Fail" +  strftime("%Y-%m-%d %H:%M:%S",  gmtime())
            commonFns.Resultsupdate(constants.Data['testresult'], filename)
            commonFns.screenshot(testcaseDescription)
        else:
            print '############0'
            #logging.debug("consumer4.0 launched")
            print "Not able to take screen shot"
            filename = testcaseDescription +  "pass" +  strftime("%Y-%m-%d %H:%M:%S",  gmtime())
            commonFns.Resultsupdate(constants.Data['testresult'], filename)'''




if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.verify(constants.Data["bundleid"])
    commonFns.quitApplication(constants.Data["bundleid"])
    if commonFns.launchApplication(constants.Data["bundleid"]):
        print "pass"
    else:
        print "fail"
