import commonFns
import constants
import os
import atomac.ldtp as ldtp
import time
import commands
import atomac
import unittest
import os
if __name__ == "__main__":
    #1st test case to be pass
    _installflag = constants.Data.get('installbuild-flag')
    if _installflag == 0:
        print "Now i am installing new build from QA server"

    else:
        HomeTabobjects = []
        MacSecurityTabObjects = []
        AccountTabObjects = []
        _filepath = commonFns.checkFileExits(constants.Data.get('xmlfilepath'))
        _buildinstalled_in_system = commonFns.xmlparsing(_filepath, constants.Data.get('buildnumber'))
        print ("Build number installed: %s" % _buildinstalled_in_system)
        commonFns.launchApplication(constants.Data["bundleid"])
        _refrenceid = commonFns.getApplicationReferenceID(constants.Data["bundleid"])
        print "_ref", _refrenceid
        _windowname = commonFns.getApplicationwindowId(_refrenceid)
        _title = commonFns.getApplicatontitle(_windowname)
        print ("Installed: %s" % _title)
        #2secnd test case
        HomeTabobjects = commonFns.getAppButtons(_windowname)
        commonFns.atomacclick(HomeTabobjects[6])
        print "Verifying Device Status "
        ldtp.wait(3)
        DeviceStatus_Descriptions = commonFns.devicesSatusVerification(_windowname)
        for info in DeviceStatus_Descriptions:
            print info
        print "Verifying protectMoreDevices"
        commonFns.protectMoreDevices(HomeTabobjects[7])
        print "Verifying pcorMacVerification"
        commonFns.pcorMacVerification(_windowname, _refrenceid, constants.Data["icon"], constants.Data["email"])
        childwindows = commonFns.getApplicationwindowId(_refrenceid)
        protectdevicewindowbuttons = commonFns.getAppButtons(childwindows)
        commonFns.atomacclick(protectdevicewindowbuttons[0])
        ldtp.wait(10)
        newbuttons = commonFns.getAppButtons(childwindows)
        #ldtp.wait(3)
        commonFns.atomacclick(newbuttons[0])
        ldtp.wait(5)
        #====
        commonFns.atomacclick(HomeTabobjects[0])
        print "Verifying deepDevice"
        deep_device = commonFns.deepDevice(_windowname, _refrenceid)
        ldtp.wait(4)
        deep_device_all_objects = commonFns.getAllObjects(deep_device)
        deep_deivce_buttons = commonFns.getAppButtons(deep_device)
        commonFns.atomacclick(deep_deivce_buttons[1])
        ldtp.wait(4)
        commonFns.atomacclick(deep_deivce_buttons[2])
        ldtp.wait(2)
        print "Verifying Notification"
        notification_content = commonFns.verifynotification(HomeTabobjects[3])
        print "Verifying contextualhelp"
        ldtp.wait(4)
        commonFns.contextualhelpverificationhome(_windowname, HomeTabobjects[4])
        ldtp.wait(7)
        print "Running EicherTest"
        commonFns.eichertest()
        Mcafee_Reporter_reference = commonFns.ReporterReference(constants.Data['Reporterpid'])
        print "Parsing Notification Window"
        commonFns.ReporterParsing(Mcafee_Reporter_reference)
        commonFns.atomacclick(HomeTabobjects[0])
        print "Verifiying Run a scan in home Tab"
        commonFns.homerunascan(_windowname, _refrenceid)
        ldtp.wait(4)
        print "Verifiying Custom Scan in home Tab"
        commonFns.homeCustomScan(_windowname, _refrenceid)

        print "Verifiying Home Updates home Tab"
        commonFns.homeupdates(_windowname, _refrenceid)
        print "Verifiying Mac Security qurantine home Tab"
        #commonFns.MacSecurityqurantine(_windowname, _refrenceid)
        #ldtp.wait(1)
        #globalsettings_content = commonFns.getApplicatontitle(HomeTabobjects[5])
        #commonFns.verifysubscription(DeviceStatus_Descriptions)
        commonFns.globalsettings(HomeTabobjects[5])
        commonFns.quitApplication(constants.Data["bundleid"])
        ############################################
        #print "HomeTabobjects", HomeTabobjects
        #print HomeTabobjects[3].AXTitle
        #commonFns.contextualhelpverification(_windowname,HomeTabobjects[3])
        #print "HomeTabobjects", HomeTabobjects
        #commonFns.atomacclick(HomeTabobjects[1])
        #MacSecurityTabObjects =commonFns.getAppButtons(_windowname)
        #print "MacSecurityTabObjects", MacSecurityTabObjects
        #commonFns.atomacclick(HomeTabobjects[2])
        #AccountTabObjects = commonFns.getAppButtons(_windowname)
        #print "AccountTabObjects", AccountTabObjects
        #THEN PROTECT MORE DEVICES
        '''commonFns.atomacclick(HomeTabobjects[2])
        AccountTabbuttons = commonFns.getAppButtons(_refrenceid)
        commonFns.atomacclick(AccountTabbuttons[9])
        ldtp.wait(5)
        content = commonFns.Accountabout(_refrenceid)
        print "content", content'''



        


