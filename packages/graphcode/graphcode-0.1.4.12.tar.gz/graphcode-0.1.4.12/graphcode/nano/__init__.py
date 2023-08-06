'''
The License For Peaceful Use

Copyright (c) 2003-2217 Ryeojin Moon
Copyright (c) 2002-3333 GraphCode

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

THIS SOFTWARE IS NOT PROVIDED TO ANY ENTITY OR ANY PERSON TO THREATEN, INCITE, 
PROMOTE, OR ACTIVELY ENCOURAGE VILOENCE, TERRORISM, OR OTHER SERIOUS HARM. 
IF NOT, THIS SOFTWARE WILL NOT BE PERMITTED TO USE. IF NOT, THE BENIFITS OF
ALL USES AND ALL CHANGES OF THIS SOFTWARE IS GIVEN TO THE ORIGINAL AUTHORS
WHO HAVE OWNED THE COPYRIGHT OF THIS SOFTWARE. THIS RESTRICTION CAN BE REMOVED
WITH THE ORIGINAL AUTHORS' AGREEMENT BY A DOCUMENT.
===
Created by September 21st, 2002
Revised on January 4th, 2003 by @author: ryeojin1@gmail.com
'''
from graphcode.logging import setLogLevel, logDebug, logInfo, logError, raiseValueError, logWarn, logCritical, logException, logExceptionWithValueError

from graphcode.path import getWorkDirname, getGraphCodeDirname, listDir

from graphcode.nano.render import render

from graphcode.lib import getKwargs, loadDirAsModule, isNamingForApps, isValidTcpPortNumber, isNamingForAction, isValidHttpFormat, isValidHttpRequest

import graphcode.sslCertificate as sslCertificate

import sys
import inspect
from os import mkdir, rename
from os.path import exists, join, expanduser, abspath, dirname, basename, split

import time
from pytz import timezone
from datetime import datetime

import json

import shutil
from uuid import uuid4

__nanoWorkingDirname__ = getWorkDirname()

def setWorkingDirnameToGrapheCode():
  global __nanoWorkingDirname__
  __nanoWorkingDirname__ = getGraphCodeDirname()
  logDebug("__nanoWorkingDirname__:[{}] is set".format(__nanoWorkingDirname__))
  
  return __nanoWorkingDirname__
  
def setWorkingDirnameToDefault():
  global __nanoWorkingDirname__
  __nanoWorkingDirname__ = getWorkDirname()
  logDebug("__nanoWorkingDirname__:[{}] is set".format(__nanoWorkingDirname__))
  
  return __nanoWorkingDirname__
  
def setWorkingDirname(dirname):
  if exists(expanduser(dirname)):
    global __nanoWorkingDirname__
    __nanoWorkingDirname__ = expanduser(dirname)
    logDebug("__nanoWorkingDirname__:[{}] is set".format(__nanoWorkingDirname__))
    
    return __nanoWorkingDirname__
  
  else:
    raiseValueError("dirname:[{}] is existing".format(expanduser(dirname)))
  
def getWorkingDirname():
  global __nanoWorkingDirname__
  logDebug("__nanoWorkingDirname__:[{}] is set".format(__nanoWorkingDirname__))
  
  return __nanoWorkingDirname__

def register(**kwargs):
  appName = getKwargs(name="appName", kwargs=kwargs)
  listForActions = getKwargs(name="listForActions", kwargs=kwargs)
  portNumber = getKwargs(name="portNumber", kwargs=kwargs)
  sslMode = getKwargs(name="sslMode", kwargs=kwargs)
  debugMode = getKwargs(name="debugMode", kwargs=kwargs)
  httpRequestFormat = getKwargs(name="httpRequestFormat", value="HTML", kwargs=kwargs)
  listForhttpRequest = getKwargs(name="listForhttpRequest", value=["GET","POST"], kwargs=kwargs)
  
  appName = appName.strip()
  
  if isNamingForApps(appName):
    dirnameForAppRoot = join(__nanoWorkingDirname__, "nanos")
  
  if exists(dirnameForAppRoot):
    if portNumber == None:
      listForUsedPorts = []
      for thisAppName in listDir(dirnameForAppRoot, type = "dir"):
        if thisAppName.startswith("_"):
          logDebug("thisAppName:[{}] ignored".format(thisAppName))
        
        else:
          listForThisAppName = thisAppName.split("__")
          
          thisPortNumber = None
          for thisItem in listForThisAppName[1:]:
            try:
              thisPortNumber = int(thisItem)
              logDebug("appName:[{}]\tthisAppName:[{}]\tthisPortNumber:[{}]".format(appName, thisAppName, thisPortNumber))
              break
            except:
              continue
          
          if thisPortNumber == None:
              raiseValueError("appName:[{}]\tthisAppName:[{}]\tportNumber is not found".format(appName, thisAppName))
            
          elif thisPortNumber > 8000:
            if appName == listForThisAppName[0]:
              raiseValueError("appName:[{}] is already used. If you want to use the same appName, please specify the portNumber instead of 'None'".format(appName))
            else:
              listForUsedPorts.append(thisPortNumber)
      
      if len(listForUsedPorts) > 0:
        portNumber = sorted(listForUsedPorts)[-1] + 1
        logDebug("appName:[{}]\tthisPortNumber:[{}] is set".format(appName, thisPortNumber))
          
      if portNumber == None:
        if __nanoWorkingDirname__ == getGraphCodeDirname():
          portNumber = "3391"
        else:
          portNumber = "8001"
        
    
    elif isValidTcpPortNumber(portNumber):
      for thisAppName in listDir(dirnameForAppRoot, type = "dir"):
        if "{}".format(portNumber) == thisAppName.split("__")[-1]:
          raiseValueError("portNumber is already registered to thisAppName:[{}]".format(thisAppName))
    
    else:
      raiseValueError("unexpected portNumber:[{}]".format(portNumber))
    
  else:
    f = open(join(getGraphCodeDirname(), "LICENSE"), "r")
    textForLicense = f.read()
    f.close()
    
    for thisSubDirname in ["", "_filters_"]:
      mkdir(join(dirnameForAppRoot, thisSubDirname))
      logDebug("dirnameForApp:[{}] is created".format(join(dirnameForAppRoot, thisSubDirname)))
    
      if thisSubDirname in ["_filters_"]:
        shutil.copyfile(join(getGraphCodeDirname(), "nano", "filters.py"), join(dirnameForAppRoot, thisSubDirname, "__init__.py"))
      
      else:
        f = open(join(dirnameForAppRoot, thisSubDirname, "__init__.py"), "w")
        f.write("'''\n"+ textForLicense + """
===
Created by September 21st, 2002
Revised on Janurary 4th, 2003 by @author: ryeojin1@gmail.com
'''
from graphcode.logging import setLogLevel, logDebug, logInfo, logError, raiseValueError, logWarn, logCritical, logException, logExceptionWithValueError
""")
        f.close()
    
    # Copy LICENSE to the app root
    f = open(join(dirnameForAppRoot, "LICENSE"), "w")
    f.write(textForLicense)
    f.close()
    
    if portNumber == None:
      if __nanoWorkingDirname__ == getGraphCodeDirname():
        portNumber = "3391"
      else:
        portNumber = "8001"
      logDebug("appName:[{}] and portNumber:[{}] are set".format(appName, portNumber))
    
    elif isValidTcpPortNumber(portNumber):
      logDebug("appName:[{}] and portNumber:[{}] are set".format(appName, portNumber))
    
    else:
      raiseValueError("unexpected portNumber:[{}]".format(portNumber))
  
  for thisAppName in listDir(dirnameForAppRoot, type = "dir"):
    thisAppName_list = thisAppName.split("__")
    if thisAppName_list[0] in [appName] and thisAppName_list[-1] in [portNumber]:
      raiseValueError("appName:[{}:[{}] is already used".format(appName, portNumber))
    elif thisAppName_list[0] in [appName]:
      logWarn("appName:[{}] is used at thisAppName:[{}]".format(appName, thisAppName))
    elif thisAppName_list[-1] in [portNumber]:
      raiseValueError("portNumber:[{}] is already used at thisAppName:[{}]".format(portNumber, thisAppName))
      
  f = open(join(getGraphCodeDirname(), "LICENSE"), "r")
  textForLicense = f.read()
  f.close()
  
  if debugMode in [True]:
    if sslMode in [True]:
      dirnameForApp = join(dirnameForAppRoot, "{}__{}__SSL__DEBUG".format(appName, portNumber))
    else:
      dirnameForApp = join(dirnameForAppRoot, "{}__{}__DEBUG".format(appName, portNumber))
  elif sslMode in [True]:
    dirnameForApp = join(dirnameForAppRoot, "{}__{}__SSL".format(appName, portNumber))
  else:
    dirnameForApp = join(dirnameForAppRoot, "{}__{}".format(appName, portNumber))
  
  for subDirname in ["", "_filters_", "_static_"]:
    mkdir(join(dirnameForApp, subDirname))
    logDebug("appName:[{}:{}] is created at dirnameForApp:[{}]".format(join(dirnameForApp, subDirname), portNumber, dirnameForApp))
    
    if subDirname in ["_static_"]:
      shutil.copytree(join(getGraphCodeDirname(),"nano","themes","default"), join(dirnameForApp, subDirname,"default"))
         
    f = open(join(dirnameForApp, subDirname, "__init__.py"), "w")
    f.write("'''\n"+ textForLicense + """
===
Created by September 21st, 2002
Revised on January 4th, 2003 by @author: ryeojin1@gmail.com
'''
from graphcode.logging import setLogLevel, logDebug, logInfo, logError, raiseValueError, logWarn, logCritical, logException, logExceptionWithValueError
""")
    f.close()
  
  if "SSL" in dirnameForApp.split("__"):
    sslCertificate.create(
      certName=appName,
      expirationDays=365, 
      countryName="US", 
      stateOrProvinceName="Washington", 
      localityName="Seattle", 
      organizationName="GraphCode", 
      organizationalUnitName="GCD", 
      serverFQDNOrYourName="GraphCode", 
      emailAddress="cert@graphcode.io",
      dirPath=dirnameForApp
      )
    
  # Copy LICENSE to the appName
  f = open(join(dirnameForApp, "LICENSE"), "w")
  f.write(textForLicense)
  f.close()
  
  # Create a seed of the appName
  f = open(join(dirnameForApp, ".seed"), "w")
  f.write("{}".format(uuid4()))
  f.close()
   
  return dirnameForApp

def deregister(appName):
  appName = appName.strip()
  
  if isNamingForApps(appName):
    dirnameForAppRoot = join(__nanoWorkingDirname__, "nanos")
    
  
  if exists(dirnameForAppRoot):
    
    listForDeregisteredAppNames = []
    for thisAppName in listDir(dirnameForAppRoot, type = "dir"):
      thisAppName_list = thisAppName.split("__")
      if thisAppName_list[0] in [appName]:
        renameForDeregisteredAppName = "_deregistered_{}_at_{}".format(thisAppName, datetime.fromtimestamp(time.time()).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H-%M-%S_%f%Z'))
        rename(join(dirnameForAppRoot, thisAppName), join(dirnameForAppRoot, renameForDeregisteredAppName))
        listForDeregisteredAppNames.append(renameForDeregisteredAppName)
        
        logWarn("[{:,}]\tappName:[{}] is deregistered".format(len(listForDeregisteredAppNames), thisAppName))
  
    if len(listForDeregisteredAppNames) == 1:
      logInfo("total {:,} appName:[{}] is deregistered".format(len(listForDeregisteredAppNames), appName))
    
    elif len(listForDeregisteredAppNames) > 1:
      logInfo("total {:,} appName:[{}]s are deregistered".format(len(listForDeregisteredAppNames), appName))
      
    else:
      logError("appName:[{}] is not found".format(appName))
    
    return listForDeregisteredAppNames
    
  else:
    raiseValueError("dirnameForAppRoot:[{}] is not found".format(dirnameForAppRoot))

def purge(appName, seed):
  appName = appName.strip()
  
  if isNamingForApps(appName):
    dirnameForAppRoot = join(__nanoWorkingDirname__, "nanos")
  
  if exists(dirnameForAppRoot):
    
    purgedCount = 0
    listForSeeds = []
    for thisAppName in listDir(dirnameForAppRoot, type = "dir"):
      if thisAppName.split("__")[0].startswith(appName):
        logWarn("appName:[{}] must be de-registered to purge".format(thisAppName))
      
      elif thisAppName.startswith("_deregistered_"):
        thisAppName_list = thisAppName[len("_deregistered_"):].split("__")
        if thisAppName_list[0] in [appName]:
          
          # read a seed of the appName
          f = open(join(dirnameForAppRoot, thisAppName, ".seed"), "r")
          thisSeed = f.read()
          f.close()
          logDebug("thisAppName:[{}]->Seed:[{}]".format(thisAppName, thisSeed))
          
          if (isinstance(seed, str) or isinstance(seed, list)) and thisSeed in seed:
            shutil.rmtree(join(dirnameForAppRoot, thisAppName))
            
            purgedCount += 1
            logWarn("[{:,}]\tappName:[{}] is purged".format(purgedCount, thisAppName[len("_deregistered_"):]))
          
          else:
            logWarn("thisApp's seed:[{}] must be matched with seed:[{}]".format(thisSeed, seed))
            listForSeeds.append(
              {
                "appName":thisAppName,
                "seed":thisSeed
                }
              )
        else:
          logWarn("thisAppName is not matched with appName:[{}]".format(thisAppName_list[0], appName))
             
    if purgedCount == 1:
      logInfo("total {:,} appName:[{}] is purged".format(purgedCount, appName))
    
    elif purgedCount > 1:
      logInfo("total {:,} appName:[{}]s are purged".format(purgedCount, appName))
      
    else:
      logError("appName:[{}] is not found or seed is not matched".format(appName))
      return listForSeeds
    
    return purgedCount
  
  else:
    raiseValueError("dirnameForAppRoot:[{}] is not found".format(dirnameForAppRoot))
  
def activate(appName, actionName, httpRequestFormat="HTML", listForhttpRequest=["GET","POST"]):
  appName = appName.strip()
  actionName = actionName.strip()
  
  if isNamingForApps(appName) and isNamingForAction(actionName) and isValidHttpFormat(httpRequestFormat):
    dirnameForAppRoot = join(__nanoWorkingDirname__, "nanos")
    httpRequestFormat = httpRequestFormat.upper()
    
  allowedHttpRequests = ""
  for thisHttpRequest in sorted(listForhttpRequest):
    if isValidHttpRequest(httpRequest=thisHttpRequest):
      #logDebug("appName:[{}]->thisHttpRequest:[{}] is supported".format(appName, thisHttpRequest))
      if allowedHttpRequests == "":
        allowedHttpRequests = "{}".format(thisHttpRequest)
      else:
        allowedHttpRequests = "{}_{}".format(allowedHttpRequests, thisHttpRequest)
  
  if allowedHttpRequests == "":
    raiseValueError("unexpected listForhttpRequest:{} because of allowedHttpRequests:[{}]".format(listForhttpRequest, allowedHttpRequests))
    
  if exists(dirnameForAppRoot):
    
    createdActionCount = 0
    for thisDirnameForApp in listDir(dirnameForAppRoot, type = "dir"):
      if thisDirnameForApp.split("__")[0] in [appName]:
        
        for thisDirnameForAction in listDir(join(dirnameForAppRoot, thisDirnameForApp), type = "dir"):
          if thisDirnameForAction.split("__")[0] in [actionName]:
            raiseValueError("appName:[{}]->actionName:[{}] is duplicated with thisDirnameForAction:[{}]".format(appName, actionName, thisDirnameForAction))
        
        dirnameForAction = join(join(dirnameForAppRoot, thisDirnameForApp), "{}__{}__{}".format(actionName, httpRequestFormat, allowedHttpRequests))
        mkdir(dirnameForAction)
        createdActionCount += 1
        logDebug("appName:[{}]->dirnameForAction:[{}] is created successfully".format(appName, dirnameForAction))
        
        if httpRequestFormat in ["HTML"]:
          for childDirname in ["_css_", "_img_", "_js_"]:
            mkdir(join(dirnameForAction, childDirname))
            logDebug("appName:[{}]\tactionName:[{}]->child directory:[{}] is created".format(appName, join(dirnameForAction, childDirname), actionName, childDirname))
            
        f = open(join(getGraphCodeDirname(), "LICENSE"), "r")
        textForLicense = f.read()
        f.close()
        
        f = open(join(dirnameForAction, "__init__.py"), "w")
        f.write("'''\n"+ textForLicense + """
===
Created by September 21st, 2002
Revised on January 4th, 2003 by @author: ryeojin1@gmail.com
'''
from graphcode.logging import setLogLevel, logDebug, logInfo, logError, raiseValueError, logWarn, logCritical, logException, logExceptionWithValueError

from graphcode.nano.response import response

import time

from uuid import uuid4

def view():
  reqeustId = uuid4()
  logDebug("#requestId:[{}]".format(reqeustId))
  
  dictForResponse = {}
  
  return response(
    reqeustId = reqeustId,
    dictForResponse = dictForResponse,
    rulePath=__file__, 
    httpRequestFormat=""" + "\"{}\"".format(httpRequestFormat) +""",
    __beginTime__ = time.time()
    )
""")
        f.close()
  
    
    if createdActionCount == 1:
      logInfo("total {:,} actionName:[{}/{}] is created".format(createdActionCount, appName, actionName))
    
    elif createdActionCount > 1:
      logInfo("total {:,} actionName:[{}/{}]s are created".format(createdActionCount, appName, actionName))
    
    else:
      raiseValueError("actionName:[{}/{}] is not created".format(appName, actionName))
      
    return dirnameForAction
  
  else:
    raiseValueError("dirnameForAppRoot:[{}] is not found".format(dirnameForAppRoot))
  
def deactivate(appName, actionName):
  appName = appName.strip()
  actionName = actionName.strip()
  
  if isNamingForApps(appName) and isNamingForAction(actionName):
    dirnameForAppRoot = join(__nanoWorkingDirname__, "nanos")
  
    deactivatedCount = 0
    for thisDirnameForApp in listDir(dirnameForAppRoot, type = "dir"):
      if thisDirnameForApp.split("__")[0] in [appName]:
        
        for thisDirnameForAction in listDir(join(dirnameForAppRoot, thisDirnameForApp), type = "dir"):
          if thisDirnameForAction.split("__")[0] in [actionName]:
            dirnameForAction = join(join(dirnameForAppRoot, thisDirnameForApp), thisDirnameForAction)
            
            rename(dirnameForAction, join(join(dirnameForAppRoot, thisDirnameForApp), "_deactivated_{}_at_{}".format(thisDirnameForAction, datetime.fromtimestamp(time.time()).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H-%M-%S_%f%Z'))))
          
            deactivatedCount += 1
            logWarn("[{:,}]\taction:[{}] is deactivated".format(deactivatedCount, dirnameForAction))
          
    if deactivatedCount == 1:
      logInfo("total {:,} action:[{}/{}] is deactivated".format(deactivatedCount, appName, actionName))
    
    elif deactivatedCount > 1:
      logInfo("total {:,} action:[{}/{}]s are deactivated".format(deactivatedCount, appName, actionName))
    
    else:
      logError("action:[{}/{}] is not found".format(appName, actionName))
  
    return deactivatedCount

  else:
    raiseValueError("dirnameForAppRoot:[{}] is not found".format(dirnameForAppRoot))
    
def remove(appName, actionName):
  appName = appName.strip()
  actionName = actionName.strip()
  
  if isNamingForApps(appName) and isNamingForAction(actionName):
    dirnameForAppRoot = join(__nanoWorkingDirname__, "nanos")
    
    deletedCount = 0
    for thisDirnameForApp in listDir(dirnameForAppRoot, type = "dir"):
      #logDebug("#thisDirnameForApp:[{}]".format(thisDirnameForApp))
      
      if thisDirnameForApp.split("__")[0] in [appName]:
        for thisDirnameForAction in listDir(join(dirnameForAppRoot, thisDirnameForApp), type = "dir"):
          #logDebug("#thisDirnameForApp:[{}]->thisDirnameForAction:[{}]".format(thisDirnameForApp, thisDirnameForAction))
          
          if thisDirnameForAction.startswith("_deactivated_"):
            #logDebug("#thisDirnameForAction:[{}]".format(thisDirnameForAction[len("_deactivated_"):].split("_")[0]))
            
            if thisDirnameForAction[len("_deactivated_"):].split("__")[0] in [actionName]:
              dirnameForAction = join(join(dirnameForAppRoot, thisDirnameForApp), thisDirnameForAction)
              
              shutil.rmtree(dirnameForAction)
              
              deletedCount += 1
              logWarn("[{:,}]\taction:[{}] is deleted".format(deletedCount, dirnameForAction))
            
    if deletedCount == 1:
      logInfo("total {:,} action:[{}/{}] is deleted".format(deletedCount, appName, actionName))
    
    elif deletedCount > 1:
      logInfo("total {:,} action:[{}/{}]s are deleted".format(deletedCount, appName, actionName))
      
    else:
      logError("action:[{}/{}] is not found".format(appName, actionName))
    
      return deletedCount
    
  else:
    raiseValueError("dirnameForAppRoot:[{}] is not found".format(dirnameForAppRoot))
    
def create(**kwargs):
  appName = getKwargs(name="appName", kwargs=kwargs)
  listForActions = getKwargs(name="listForActions", kwargs=kwargs)
  portNumber = getKwargs(name="portNumber", kwargs=kwargs)
  sslMode = getKwargs(name="sslMode", kwargs=kwargs)
  debugMode = getKwargs(name="debugMode", kwargs=kwargs)
  httpRequestFormat = getKwargs(name="httpRequestFormat", value="HTML", kwargs=kwargs)
  listForhttpRequest = getKwargs(name="listForhttpRequest", value=["GET","POST"], kwargs=kwargs)
  
  
  listForActivatedActions = []
  try:
    register(
      appName=appName, 
      listForActions=listForActions,
      portNumber=portNumber,
      sslMode=sslMode,
      debugMode=debugMode,
      httpRequestFormat=httpRequestFormat,
      listForhttpRequest=listForhttpRequest
      )
  except:
    return {"appName":appName, "actions":listForActivatedActions, "error":logException("failed to register appName:[{}]".format(appName))}
    
  for thisActionItem in listForActions:
    #logDebug("#type:{}:thisActionItem:[{}]".format(type(thisActionItem), thisActionItem))
    
    if isinstance(thisActionItem, str):
      activate(appName, actionName=thisActionItem, httpRequestFormat=httpRequestFormat, listForhttpRequest=listForhttpRequest)
      listForActivatedActions.append(
        {
          "actionName": thisActionItem,
          "httpRequestFormat": httpRequestFormat, 
          "listForhttpRequest": listForhttpRequest
          }
        )
    elif isinstance(thisActionItem, list):
      if len(thisActionItem) == 1:
        activate(appName, actionName=thisActionItem[0], httpRequestFormat=httpRequestFormat, listForhttpRequest=listForhttpRequest)
        listForActivatedActions.append(
          {
            "actionName": thisActionItem[0],
            "httpRequestFormat": httpRequestFormat, 
            "listForhttpRequest": listForhttpRequest
            }
          )
      elif len(thisActionItem) == 2:
        activate(appName, actionName=thisActionItem[0], httpRequestFormat=thisActionItem[1], listForhttpRequest=listForhttpRequest)
        listForActivatedActions.append(
          {
            "actionName": thisActionItem[0],
            "httpRequestFormat": thisActionItem[1], 
            "listForhttpRequest": listForhttpRequest
            }
          )
      elif len(thisActionItem) == 3:
        if isinstance(thisActionItem[2], str):
          activate(appName, actionName=thisActionItem[0], httpRequestFormat=thisActionItem[1], listForhttpRequest=thisActionItem[2].split(","))
          listForActivatedActions.append(
            {
              "actionName": thisActionItem[0],
              "httpRequestFormat": thisActionItem[1], 
              "listForhttpRequest": thisActionItem[2]
              }
            )
        elif isinstance(thisActionItem[2], list):
          activate(appName, actionName=thisActionItem[0], httpRequestFormat=thisActionItem[1], listForhttpRequest=thisActionItem[2])
          listForActivatedActions.append(
            {
              "actionName": thisActionItem[0],
              "httpRequestFormat": thisActionItem[1], 
              "listForhttpRequest": thisActionItem[2]
              }
            )
        else:
          logError("unexpected thisActionItem(len:{:,}):[{}]".format(len(thisActionItem), thisActionItem))
      else:
        logError("unexpected thisActionItem(len:{:,}):[{}]".format(len(thisActionItem), thisActionItem))

    elif isinstance(thisActionItem, dict):
      if "actionName" in thisActionItem.keys():
        thisActionName = thisActionItem["actionName"]
        
        if "httpRequestFormat" in thisActionItem.keys():
          thisHttpRequestFormat = thisActionItem["httpRequestFormat"]
        else:
          thisHttpRequestFormat = httpRequestFormat
        
        if "listForhttpRequest" in thisActionItem.keys():
          thisListForhttpRequest = thisActionItem["listForhttpRequest"]
        else:
          thisListForhttpRequest = httpRequestFormat
        
        activate(appName, actionName=thisActionName, httpRequestFormat=thisHttpRequestFormat, listForhttpRequest=thisListForhttpRequest)
        listForActivatedActions.append(
          {
            "actionName": thisActionName,
            "httpRequestFormat": thisHttpRequestFormat, 
            "listForhttpRequest": thisListForhttpRequest
            }
          )
        
      else:
        logError("'actionName' is not found at thisActionItem.keys():[{}]".format(thisActionItem.keys()))
        
    else:
      logError("unexpected type:{}:thisActionItem:[{}]".format(type(thisActionItem), thisActionItem))
  
  return {"appName":appName, "actions":listForActivatedActions}

  