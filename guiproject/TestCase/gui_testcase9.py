import sys
import os
import atomac.ldtp as ldtp
testcaseName = sys.argv[0][:-3]
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import constants
import commonFns
import logging
from time import gmtime, strftime
testcaseDescription = "Reporter window Parsing "

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

    def verify(self, reporterpid):
        refportref = commonFns.ReporterReference(reporterpid)
        commonFns.ReporterParsing(refportref)


    def reporting(self):
        print "Executing %s" % testcaseName, ":" + testcaseDescription

if __name__ == "__main__":
    testcaseobj = TestCase()
    testcaseobj.reporting()
    testcaseobj.launch(constants.Data["bundleid"])
    ref = testcaseobj.appRef(constants.Data["bundleid"])
    window = testcaseobj.appwindow(ref)
    testcaseobj.verify(constants.Data["Reportercommand"])
    filename = testcaseDescription + "pass" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    commonFns.Resultsupdate(constants.Data['testresult'], filename)


