import re
import os
import os.path
import atomac
import logging
import xml.etree.ElementTree as ET
import time
import subprocess
import atomac.ldtp as ldtp
import commands
from subprocess import Popen, PIPE
from subprocess import call
from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
timeout = 15
logFileMode='w'
#driver = webdriver.Firefox()
logFormat = '%(asctime)s %(levelname)-8s %(message)s'
logDateFmt='%d %b %H:%M:%S'
logfile = '/Users/suresh/Desktop/guiproject/logging/logfile.log'
logLevel = logging.INFO
logging.basicConfig(level=logLevel, format=logFormat, datefmt=logDateFmt, filename=logfile, filemode=logFileMode)

def atomachandle():
    try:
        import atomac
        _atomachandle = atomac
    except Exception as er:
        print ("not able to get atomac handle")
        return False
    return _atomachandle

def launchApplication(Cbundleid):
    try:
        atomac.launchAppByBundleId(Cbundleid)
        logging.info('Application launched successfully')
        ldtp.wait(3)
    except Exception as er:
        logging.info('Not able to launch Application, Please check Application added in Accessbility')
def getApplicationReferenceID(Cbundleid):
    try:
        ReferenceID = atomac.getAppRefByBundleId(Cbundleid)
        #print ("ReferenceID of the Application : %s" % ReferenceID)
        logging.info("Application RefferenceID : %s" % ReferenceID)
    except Exception as er:
        logging.info('Not able to get Application ReferenceID')
        return False
    return ReferenceID

def getAppRefByPidofapp(processid):
    try:
        _pidreference = atomac.getAppRefByPid(processid)
        logging.info("Application RefferenceID : %s" % _pidreference)
    except Exception as er:
        logging.info('Not able to get Application ReferenceID')
        return False
    return _pidreference
def getApplicationwindowId(ReferenceID):
    try:
        ldtp.wait(5)
        window = ReferenceID.windows()[0]
        logging.info("Application id of the window : %s" % window)
    except Exception as er:
        logging.info('Not able to get window name  of Application')
        return False
    return window

def getChildwindows(ReferenceID):
    try:
        ldtp.wait(3)
        window = ReferenceID.windowsR()[0]
        logging.info("child windows : %s" % window)
    except Exception as er:
        logging.info('Not able to get child windows')
        return False
    return window

def getApplicatontitle(window):
    try:
        title = window.AXTitle
        logging.info("Titile is : %s" % title)
    except Exception as er:
        logging.info('Not able to get  Title')
        return False
    return title

def getAppButtons(window):
    try:
        AppButtons = window.buttonsR()
        logging.info("Button got from the current screen of the Application: %s" % AppButtons)
    except Exception as er:
         print("Not able to get the application buttons, please check getApplicationwindowId")
         return False
    return AppButtons
def getAllObjects(window):
    try:
        AppButtons = window.findAllR()
        logging.info("All objects: %s" % AppButtons)
    except Exception as er:
        return False
        print("not able to get All objects")
    return AppButtons
def getMenubuttons(allbuttons):
    try:
        menubuttons = allbuttons[0:3]
        actualbuttons = []
        for words in menubuttons:
            actualbuttons.append(str(words).split("\'")[1])
        logging.info("Menu buttons of the application: %s" % actualbuttons)
    except Exception as er:
        print("Not able to get Menu buttons")
    return False
    return actualbuttons

def clickonbutton(titleobj, buttontoclick):
    try:
        ldtp.click(titleobj,buttontoclick)
        logging.info("Clicked on : %s" % buttontoclick)
    except Exception as er:
        print ("Not able to click on button")
def atomacclick(objecttoclick):
    try:
        objecttoclick.Press()
        #print "clicked on : %s" %objecttoclick
    except Exception as er:
        print "Not able to click on: %s" %objecttoclick
def verifyGuiObjects(object,one,two,three):
    try:
        if one and two and three in object:
            print "GUI objects verified: %s" % one, two, three
    except Exception as er:
        print"GUI objects are not present in GUI"
    return False

def fileRenameandReplace(filename,newfilename):
    try:
        os.rename(filename,newfilename)
        logging.info("Json file renamed in PD path")
    except Exception as er:
        print ("Not able to rename the json file ")
    return False

def killprocess(ReferenceID):
    '''os.system("ps -eaf|grep -i 'Mcafee'|grep -v grep|awk '{print $2}'|xargs kill")
    date 1102122317'''
    pass
def checkFileExits(file):
    try:
        if os.path.isfile(file):
            logging.info("File Exist in given path: %s" % file)
        else:
            print "File not Exist in the given path"
    except Exception as er:
        return False
    return file
def xmlparsing(xmlpath, valuetoget):
    try:
        _Handle = ET.parse(xmlpath)
        rootelement = _Handle.getroot()
        number = rootelement[valuetoget].text
        return number
        #return _Handle
    except Exception as er:
        print "Not able to Read /usr/local/McAfee/ProductConfig.xml file"

def loglogparsing(filepath):
    try:
        with open(filepath) as Masterinstaller:
            for line in Masterinstaller:
                if re.search("Successfully", line):
                    logobject = line
                    logging.info("Output from MasterInstaller log: %s" % objecttoidentify)
    except Exception as er:
        print "Unable to Read the MasterInstaller.log"
    return logobject

def getDriver():
    try:
        driverhandle = driver
    except Exception as er:
        return False
    return driverhandle

def Launchurl(url):
    try:
        driver.get(url)
        driver.implicitly_wait(45)
    except Exception as er:
        return False
        print "Not able to launch URL"
def login(login,username,password,button):
    try:
        driver.find_element_by_xpath(login).click()
        driver.find_element_by_xpath(username).send_keys(username)
        driver.find_element_by_xpath(password).send_keys(password)
        loginbutton = driver.find_element_by_name(button).click()
        waituntilelementload(loginbutton)
    except Exception as er:
        return False
    print "Not able to login"
def downloadbuild(downloadmacbuildbuttonid):
    try:
        Downloadbuttonpresent = EC.presence_of_element_located((By.ID, downloadmacbuildbuttonid))
        driver.find_element_by_id(downloadmacbuildbuttonid).click()
        WebDriverWait(driver, timeout).until(Downloadbuttonpresent)
    except TimeoutException:
        print "timeout"
def GetserialKey(ulaacceptcheckbox):
    try:
        ulaacceptcheckbox = EC.presence_of_element_located((By.ID, ulaacceptcheckbox))
        driver.find_element_by_id(ulaacceptcheckbox).click()
        WebDriverWait(driver, timeout).until(ulaacceptcheckbox)
    except TimeoutException:
        print "not able to clcik on", ulaacceptcheckbox
def waituntilelementload(elementtoload,driver):
    try:
        objecttopresent = EC.presence_of_element_located((By.XPATH,elementtoload))
        driver.find_element_by_xpath(elementtoload).click()
        WebDriverWait(driver,timeout=15).until(elementtoload)
    except TimeoutException:
        return objecttopresent

def findelement(element,listname):
    try:
        index_element = listname.index(element)
        return index_element
    except ValueError:
        return None
def getpid(command):
    try:
        _pidof = executeCommand(command)
    except Exception as er:
        print (" not able to get pid")
        return False
        print "_pidof", _pidof
    return _pidof
def getMcafeedmgfilename(dmgpath, dmgfilename):
    try:
        for root, dirs, files in os.walk(dmgpath):
            for dmg in files:
                if dmg.endswith(dmgfilename):
                    dmginstallername = dmgfilename
    except Exception as er:
        logging.DEBUG("dmg")
    return False
    return dmginstallername
def productUninstall(command):
    try:
        Executingbysubprocess(command)
        print "uninstallcommand". command
    except Exception as er:
        print "Not able to uninstall the product"
def convertlisttostring(listtostrip):
    try:
        newlist = []
        newlist = listtostrip
        findobjectnames = str(newlist).replace("\\", "")
        print("list strip done")
    except Exception as er:
        print "not able to strip list"
    return False
    return findobjectnames

def getInstallerbuttons(pidofmasterinstaller):
    dmgwindow = atomac.getAppRefByPid(pidofmasterinstaller)
    Masterinstallerbuttons = getAppButtons(dmgwindow)
    return Masterinstallerbuttons

def handleInstallerinterrruptions(window,texttosearch,fileexist):
    pass

def entertext(Title,objectname,stringtoenter):
    try:
        ldtp.enterstring(Title,objectname,stringtoenter)
        logging.DEBUG("entered string")
    except Exception as er:
        logging.DEBUG("Not able to enter the string in %")

def readTextFields(window):
    try:
        textlist = []
        textlist = window.textFields()
        logging.DEBUG("textfields in current window")
    except Exception as er:
        logging.DEBUG("Not able to get textfields in current window")
    return False
    return textlist

def readStaticText(window):
    try:
        statictextofcurrentwindow = window.staticTextsR()
        logging.DEBUG("Statictext in the current window")
    except Exception as er:
        logging.DEBUG("Not able to read the static text")
    return False
    return statictextofcurrentwindow

def pdValidation():
    pass

def readingtext():
    #Need to get text from multiple places
    #
    #if license key error
    pass

def rtsobjects():
    pass

def Firewallobjects():
    pass

def Automaticupdatesobjects():
    pass

def scheduledscansobjects():
    pass

def MacSecurityrunascan(window,referenceid):
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[52])
        ldtp.wait(2)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[0])
    except Exception as er:
        return False
def MacSecurityCustomScan(window,referenceid):
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[52])
        ldtp.wait(2)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[0])
    except Exception as er:
        print "Not able to click on MacSecurityCustomScan"
    return False
def MacSecurityqurantine(window,refrenceid):
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[52])
        Quarantine_window = getChildwindows(refrenceid)
        Quarantine_window_buttons = getAppButtons(Quarantine_window)
        ldtp.wait(3)
        atomacclick(Quarantine_window_buttons[0])
        ldtp.wait(3)
        atomacclick(Quarantine_window_buttons[1])
        ldtp.wait(3)
        atomacclick(Quarantine_window_buttons[5])
        ldtp.wait(3)
        atomacclick(Quarantine_window_buttons[6])
    except Exception as er:
        print "Not able to click on MacSecurityqurantine"
    return False
def MacSecurityhistory(window,refrenceid):
    try:
        atomacclick(window[44])
        History_window = getChildwindows(refrenceid)
        History_window_buttons = getAppButtons(History_window)
        print "History_window_buttons", History_window_buttons
        atomacclick(History_window_buttons[0])
        ldtp.wait(3)
        atomacclick(History_window_buttons[2])
        ldtp.wait(3)
        atomacclick(History_window_buttons[3])
        ldtp.wait(3)
    except Exception as er:
        print "Not able to click on MacSecurityhistory"
    return False
def eichertest():
    try:
        eicher = ('echo ZQZXJVBVT >> mcafee1.txt', 'echo ZQZXJVBVT >> mcafee2.txt','echo ZQZXJVBVT >> mcafee2.txt')
        for test in eicher:
         executeCommand(test)
    except Exception as er:
        print "Not able to do install check"
    return False
def Accountmyaccount():
    pass

def Accountabout(referenceid):
    try:
        content = []
        childwindow = getChildwindows(referenceid)
        childwindowdata = readStaticText(childwindow)
        print "childwindowdata", childwindowdata
        for i in childwindowdata:
            content.append(i)
        #childwindowobjects = getAllObjects(childwindow)
        #print dir(childwindowobjects[5])
    except Exception as er:
        return False
    return content
def Daysleftverification():
    pass

def verifysubscriptionstatusinaccounttab():
    pass
def verifysubscriptioninhomedevicestatus(sub):
    try:
        if "Subscription Active" in sub:
            print " Hi chetan You have Active subscription"
        else:
            print " your subscription is not active "
    except Exception as er:
        print("not able to get subscription details")
        return False
def homerunascan(window,referenceid):
    allbuttons = getAppButtons(window)
    atomacclick(allbuttons[14])
    ldtp.wait(3)
    Runwindow = getChildwindows(referenceid)
    buttons = getAppButtons(Runwindow)
    atomacclick(buttons[0])
    buttons = getAppButtons(Runwindow)
    ldtp.wait(4)
    atomacclick(buttons[1])
def homeCustomScan(window,referenceid):
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[52])
        ldtp.wait(2)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[1])
    except Exception as er:
        print("Not able to click on HomeCustomScan")
        return False
def homeupdates(window, referenceid):
    try:
        allobjects = getAllObjects(window)
        atomacclick(allobjects[53])
        ldtp.wait(2)
        Runwindow = getChildwindows(referenceid)
        buttons = getAppButtons(Runwindow)
        atomacclick(buttons[0])
        buttons = getAppButtons(Runwindow)
        ldtp.wait(2)
        atomacclick(buttons[1])
    except Exception as er:
        print("Not able to click on MacSecurityhistory")
        return False
def verifynotification(notificationbutton):
    try:
        atomacclick(notificationbutton)
        ldtp.wait(3)
        content = notificationbutton.AXTitle
        ldtp.wait(1)
    except Exception as er:
        logging.DEBUG("Not able to click on notification object")
        return False
    return content
def contextualhelpverificationhome(window,contextualhelpbutton):
    try:
        atomacclick(contextualhelpbutton)
        appbuttons = getAppButtons(window)
        for i in range(1,6):
            ldtp.wait(2)
            atomacclick(appbuttons[27])
        appbuttons = getAppButtons(window)
        atomacclick(appbuttons[27])
    except Exception as er:
        return False
    print "Not able to click on contextualhelpverification"
def globalsettings(golbalsettingbutton):
    try:
        atomacclick(golbalsettingbutton)
        global_settings_content = getApplicatontitle(golbalsettingbutton)
    except Exception as er:
        print "Not able to get globalsettings_content"
        return False
    return global_settings_content
def deepDevice(window,ReferenceID):
    try:
        allobjects = window.findAllR()
        atomacclick(allobjects[29])
        #ldtp.wait(10)
        child = getChildwindows(ReferenceID)
        #print "allobjects", child.findAllR()
    except Exception as er:
        print "Not able to click on deepDevice"
        return False
    return child
def rtsOn():
    pass

def rtsOff():
    pass

def firewallOff():
    pass

def friewallOn():
    pass

def verifyActionCenterFirewall():
    pass

def verifyActionCenterRts():
    pass

def devicesSatusVerification(windowname):
    try:
        AppButtons = getAppButtons(windowname)
        DeviceStatus = AppButtons[10:14]
        DeviceStatus_Descriptions = []
        for device in DeviceStatus:
            Descriptionsofsettings = getApplicatontitle(device)
            DeviceStatus_Descriptions.append(Descriptionsofsettings)
    except Exception as er:
        return False
    return DeviceStatus_Descriptions
def ReporterReference(pidofreporter):
    try:
        pid_list = []
        Mcafee_Reporter_pid = getpid(pidofreporter)
        listofpid = list(Mcafee_Reporter_pid)
        pid_list.append(listofpid[1])
        split_pids_by_space = [words for segments in pid_list for words in segments.split()]
        reporter_current_pid = int(''.join(map(str,split_pids_by_space[1])))
        Mcafee_Reporter_Reference = getAppRefByPidofapp(reporter_current_pid)
    except Exception as er:
        return False
    print "Not able to get Reporter details"
    return Mcafee_Reporter_Reference
def ReporterParsing(refrenceid):
    try:
        Mcafee_Reporter_window = getApplicationwindowId(refrenceid)
        Mcafee_Reporter_buttons = getAllObjects(Mcafee_Reporter_window)
        Mcafee_Reporter_all_objects = getAllObjects(Mcafee_Reporter_window)
        table_object = Mcafee_Reporter_all_objects[18]
        table_rows = table_object.AXRows
        #for n in table_rows:
         #   print n.AXChildren
            #print n.AXValue
           #print "data", n.AXChildren
           #print "value", n.AXValue
        ldtp.wait(10)
        atomacclick(Mcafee_Reporter_all_objects[50])
    except Exception as er:
        return False
        print "Not able to Parse Reporter window"
def protectMoreDevices(button):
    try:
        atomacclick(button)
    except Exception as er:
        print "Not able to click on protectMoreDevices button"
def pcorMacVerification(window,refrenceid,objectidentifier,texttoenter):
    try:
        buttons = getAppButtons(window)
        atomacclick(buttons[8])
        childwindow = refrenceid.windowsR()
        protectMoreDevicestitle = getApplicatontitle(childwindow[0])
        entertext(protectMoreDevicestitle,objectidentifier,texttoenter)
    except Exception as er:
        return False
    print "Not able to able to send mail"
def sendsms(window,refrenceid,image,email):
    try:
        buttons = getAppButtons(window)
        atomacclick(buttons[9])
        childwindow = refrenceid.windowsR()
        protectMoreDevicesbuttons = getAppButtons(childwindow[0])
        protectMoreDevicestitle = childwindow[0].getApplicatontitle()
        ldtp.enterstring(protectMoreDevicestitle,image,email)
        #Need to write after click
    except Exception as er:
        print "Not able to send mail"

def turnOnFirewallFromActioncenter():
    pass

def turnOnRtsfromActioncenter():
    pass

def productactivate():
    pass

def mac_security_tab_status(refrenceid):
    try:
        AppButtons = getAllObjects(refrenceid)
        DeviceStatus = AppButtons[25:29]
        Descriptions = []
        for device in DeviceStatus:
            Descriptionsofsettings = getApplicatontitle(device)
            Descriptions.append(Descriptionsofsettings)
    except Exception as er:
        return False
    return Descriptions
def executeCommand(commandtoexecute):
    try:
        _output = commands.getstatusoutput(commandtoexecute)
    except Exception as er:
        print "not able to execute command"
        return False
    return _output
def Executingbysubprocess(command):
    result = subprocess.Popen(command, shell=True, stdout=PIPE).stdout
    output = result.read()
    print output

def statusupdate(filepath):
    pass
def Resultsupdate(filepath,filecontents):
    try:
        with open(filepath, 'a') as f:
            file_handler = f.writelines(filecontents + '\n')
    except Exception as er:
        return False
    return file_handler
def screenshot(filename):
    call(["screencapture", "Screenshot for" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + filename +".jpg"])

def quitApplication(Bundleid):
    atomac.terminateAppByBundleId(Bundleid)


