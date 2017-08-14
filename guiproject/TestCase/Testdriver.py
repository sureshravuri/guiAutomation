import os
import sys
import time
import atomac
import atomac.ldtp as ldtp
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import TestCases
import commonFns
import constants
import TestCases

if __name__ == "__main__":
    _installflag = constants.Data.get('installbuild-flag')
    if _installflag == 0:
        print "Going to install new build from QA Server after uninstalling existing one"
        commonFns.productUninstall(constants.Data.get('uninstallproduct'))
        ldtp.wait(10)

        #After getting serial key
        #first check build is available if it is there skip or else download the build
        #install build
        #then Run all the test cases
        #send mail with results
else:
    installed_build_number = commonFns.xmlparsing(constants.Data.get('xmlfilepath'),constants.Data.get('buildnumber'))
    print ("Triggering Consumer GUi Automation Scripts for build :%s" % installed_build_number)
    #Run all the test cases
    #send mail with results