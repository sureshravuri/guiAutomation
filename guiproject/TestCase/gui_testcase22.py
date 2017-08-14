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

testcaseDescription = "Verifying post-expiry of the product"

class TestCase():

    def __init__(self):
        pass

    def launch(self,Appbundleid):
        if not commonFns.launchApplication(Appbundleid):
            logging.error("Failed to launch Product")

    def appRef(self,Appbundleid):
        try:
            reference = commonFns.getApplicationReferenceID(Appbundleid)
        except Exception as er:
            return  False
        return reference

    def appwindow(self,reference):
        try:
            window = commonFns.getApplicationwindowId(reference)
        except Exception as er:
            return  False
        return window
    def appButtons(self,window):
        try:
            AppButtons = commonFns.getAppButtons(window)
        except Exception as er:
            return  False
        return AppButtons

    def verify(self,Appbuttons,window):
        commonFns.atomacclick(Appbuttons[6])
        device_status = commonFns.devicesSatusVerification(window)
        ldtp.wait(1)
        return device_status

    def reporting(self):
        print "Executing %s" % testcaseName, ":" + testcaseDescription

    def quit(self, Appbundleid):
        commonFns.quitApplication(Appbundleid)

if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.reporting()
    testcaseobj.launch(constants.Data["bundleid"])
    ref = testcaseobj.appRef(constants.Data["bundleid"])
    window = testcaseobj.appwindow(ref)
    buttons = testcaseobj.appButtons(window)
    device_status = testcaseobj.verify(buttons,window)
    status_parsing = device_status.encode('utf-8')
    values = str(status_parsing)
    if "Expired" in values.split:
        print "Subscription Expired"
        #writing to results file
    else:
        print "Not able find the status"
    commonFns.atomacclick(buttons[0])
    print device_status
    commonFns.atomacclick(buttons[0])
    testcaseobj.verify(buttons, window)
    filename = testcaseDescription + "pass" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    commonFns.Resultsupdate(constants.Data['testresult'], filename)
    testcaseobj.quit(constants.Data["bundleid"])
    # implement clicking in all the places of Run a scan, updates, Help and verify warning message in all 3 modules
