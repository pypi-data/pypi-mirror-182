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
Revised on Janurary 4th, 2003 by @author: ryeojin1@gmail.com
Revised on Dec 23, 2022 by @author: ryeojin1@gmail.com
'''
from graphcode.logging import setLogLevel, logDebug, logInfo, logError, raiseValueError, logWarn, logCritical, logException, logExceptionWithValueError

from graphcode.path import getWorkDirname, getGraphCodeDirname, listDir

from graphcode.nano.render import render

from graphcode.lib import getKwargs, loadDirAsModule, isNamingForApps, isValidTcpPortNumber, isNamingForAction, isValidHttpFormat, isValidHttpRequest

import inspect
from os import mkdir
from os.path import exists, join, expanduser, dirname, basename, split

import time
from pytz import timezone
from datetime import datetime

import json

import shutil
from uuid import uuid4

from multiprocessing import Process

import socket

import platform

from flask import Flask

def start():
  setLogLevel("DEBUG")
  
  if platform.system().startswith("Win"):
    tmpDir = expanduser("~\AppData\Local\Temp")
  else:
    tmpDir = expanduser("~/tmp")
    
  f = open(join(getWorkDirname(), "app.json"), "w")
  f.write("{}")
  f.close()
  
  listForNanosDirnames = []
  try:
    for appPath in listDir(join(getGraphCodeDirname(), "nanos"), type="dir"):
      if appPath.startswith("_"):
        logDebug("appPath:[{}] is ignored".format(appPath))
      else:
        listForNanosDirnames.append(join(getGraphCodeDirname(), "nanos", appPath))
  except:
    logException("failed to start at [{}]".format(getGraphCodeDirname()))
  
  try:    
    for appPath in listDir(join(getWorkDirname(), "nanos"), type="dir"):
      if appPath.startswith("_"):
        logDebug("appPath:[{}] is ignored".format(appPath))
      else:
        listForNanosDirnames.append(join(getWorkDirname(), "nanos", appPath))
  except:
    logException("failed to start at [{}]".format(getWorkDirname()))
    
  listForNanoProcesses = []
  for appPath in listForNanosDirnames:
    logDebug("appPath:[{}]".format(appPath))
    
    thisEpochTime = time.time()
    p = Process(target=processForNano, args=(appPath,))
    p.name = basename(appPath)
    p.start()
    logInfo("appName:[{}]({}) is started successfully!".format(p.name, p.pid))
    
    try:
      f = open(join(getWorkDirname(), "app.json"), "r")
      dictForApps = json.load(f)
      f.close()
    except:
      try:
        logException("failed to load 'app.json':[{}]".format(f.read()))
      except:
        logException("failed to read 'app.json'")
        
      dictForApps = {}
      
    try:
      f = open(join(getWorkDirname(), "app.json"), "w")
      
      dictForApps["{}".format(int(thisEpochTime*1000))] = {
        "appName": p.name,
        "pid": p.pid,
        "status": "started",
        "appPath": appPath,
        "startTime": thisEpochTime,
        "startDate": datetime.fromtimestamp(thisEpochTime).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%S.%f%Z')
        }
      
      json.dump(dictForApps,f)
      f.close()
      
    except:
      logException("failed to update 'app.json'")
  
    listForNanoProcesses.append(p)
  
  for p in listForNanoProcesses:
    p.join()
    logDebug("waiting for running appName:[{}]({}) completed".format(p.name, p.pid))

def processForNano(appPath):
  appName_list = basename(appPath).split("__")
  appName = appName_list[0]
  if len(appName) > 0:
    logDebug("appName:[{}]".format(appName))
    try:
      serviceIpAddress = socket.gethostbyname(appName)
    except:
      serviceIpAddress = "127.0.0.1"
      
  else:
    raiseValueError("unexpected format appPathL[{}]".format(appPath))
    
    
  debugMode = False
  sslMode = False
  if len(appName_list) >= 2:
  
    thisPortNumber = None
    for thisItem in appName_list[1:]:
      try:
        thisPortNumber = int(thisItem)
        appName.remove(thisItem)
        logDebug("appName:[{}]\tthisPortNumber:[{}]".format(appName, thisPortNumber))
        break
      except:
        continue
    
    if thisPortNumber == None:
        raiseValueError("portNumber is not found at dirname:[{}]".format(appPath))
      
    for thisItem in appName_list[1:]:
      #logDebug("#appName:[{}]\tthisItem:[{}]".format(appName, thisItem))
      if thisItem.upper() in ["DEBUG"]:
        debugMode = True
      
      elif thisItem.upper() in ["SSL"]:
        sslMode = True
        
  else:
    raiseValueError("unexpected format appPathL[{}]".format(appPath))
    
  for subDirname in ["_filters_", "_static_"]:
    if exists(join(appPath, subDirname)):
      logDebug("appName:[{}]\tdirname:[{}] is found".format(appName, join(appPath, subDirname)))
    else:
      mkdir(join(appPath, subDirname))
      logDebug("appName:[{}]\tdirname:[{}] is created".format(appName, join(appPath, subDirname)))
  
  templateDirname = join(appPath,"_templates_")
  if exists(templateDirname):
    #shutil.rmtree(templateDirname)
    logWarn("appName:[{}]\tdirname:[{}] may need to be cleaned up to remove the previous templates".format(appName, templateDirname))
  else:
    mkdir(templateDirname)
    logDebug("appName:[{}]\tdirname:[{}] is created".format(appName, templateDirname))
    
  # Reference - https://flask.palletsprojects.com/en/2.2.x/api/
  app = Flask(
    import_name = appName,
    static_folder=join(appPath, "_static_"), 
    template_folder=join(appPath, "_templates_")
    )
  
  thisParentModuleName = loadDirAsModule(dirpath=appPath)
  logDebug("appName:[{}]\tthisParentModuleName:[{}]".format(appName, thisParentModuleName))
    
  for ruleDirname in listDir(dirPath=appPath, type = "dir"):
    if ruleDirname.startswith("_"):
      logDebug("appName:[{}]\truleDirname:[{}] is ignored".format(appName, ruleDirname))
    else:
      thisModuleName = "{}.{}".format(thisParentModuleName, ruleDirname)
      
      ruleDirname_list = ruleDirname.split("__")
      
      listForMethods = ruleDirname_list[-1].split("_")
      
      thisRuleName = ruleDirname_list[0]
      if thisRuleName in ["index"]:
        thisEndpoint = "/"
      else:
        thisEndpoint = "/{}".format(thisRuleName)
      
      logDebug("appName:[{}]\tthisRuleName:[{}]\tmethods:{}\tthisEndpoint:[{}]\tthisModuleName:[{}]".format(appName, thisRuleName, listForMethods, thisEndpoint, thisModuleName))
      try:
        thisSubModule = __import__(thisModuleName, fromlist=[''])
        
      except:
        raiseValueError("failed to load module:[{}]".format(thisModuleName))
  
      try:
        # to avoid a duplicated endpoint name, each view function has a unique name instead the default function name
        thisSubModule.view.__name__ = "{}_{}".format(thisRuleName, thisSubModule.view.__name__)
        
        logDebug("thisRuleName:[{}]\tthisModuleName:[{}] is loaded with view():[{}]".format(thisRuleName, thisSubModule.__name__, thisSubModule.view.__name__))
        
        app.add_url_rule(
          rule = thisEndpoint, 
          view_func = thisSubModule.view,
          methods=listForMethods
          )
        logInfo("appName:[{}]\tthisRuleName:[{}] is added to thisEndpoint:[{}] with view_func:[{}]({})".format(appName, thisRuleName, thisEndpoint, thisSubModule.view.__name__, thisSubModule.view))
      except:
        logException("failed to add")
        
      try:
        if "HTML" in ruleDirname_list:
          logDebug("supported format:[HTML]")
          render(appPath=appPath, ruleDirname=ruleDirname)
        
        else:
          logWarn("appName:[{}]\truleDirname:[{}]\tunsupported format to render".format(appName, ruleDirname))
        
      except Exception as e:
        logException("failed to render:[{}]->Error:[{}]".format(thisRuleName, e))
        
  listForAddedFilterNames = []
  try:
    listForParentModuleNames = []
    if len(thisParentModuleName.split(".")) >= 2:
      listForParentModuleNames.append("{}._filters_".format(thisParentModuleName[:-1 - len(thisParentModuleName.split(".")[-1])]))
    listForParentModuleNames.append("{}._filters_".format(thisParentModuleName))
                                     
    for thisParentFilterModuleName in listForParentModuleNames:
      try:
        thisFilterModule = __import__(thisParentFilterModuleName, fromlist=[''])
        #logDebug("#thisParentFilterModuleName:[{}]->thisFilterModule:[{}] is loaded".format(thisParentFilterModuleName, thisFilterModule.__name__))
        for thisFilterName in dir(thisFilterModule):
          if thisFilterName.startswith("__"):
            pass#logDebug("#thisFilterName:[{}] is ignored".format(thisFilterName))
          
          elif basename(dirname(inspect.getfile(getattr(thisFilterModule, thisFilterName)))) == "_filters_":
            if thisFilterName in listForAddedFilterNames:
              logWarn("appName:[{}]->thisFilterName:[{}] is already added".format(appName, thisFilterName))
            else:
              app.add_template_filter(getattr(thisFilterModule, thisFilterName))
              listForAddedFilterNames.append(thisFilterName)
              logDebug("appName:[{}]\t(#{:,})\tthisParentFilterModuleName:[{}]->thisFilterName:[{}] is added from [{}]".format(appName, len(listForAddedFilterNames), thisParentFilterModuleName, thisFilterName, basename(dirname(inspect.getfile(getattr(thisFilterModule, thisFilterName))))))
              
          #else:
            #pass#logDebug("thisFilterName:[{}] is ignored".format(thisFilterName))
            
      except:
        logException("appName:[{}]\tunable to add filters with thisParentFilterModuleName:[{}]".format(appName, thisParentFilterModuleName))  
  except:
    logException("appName:[{}]\t[{}._filters_] module failed to load".format(appName, thisParentModuleName))
    
  logDebug("appName:[{}]\ttotal {:,} filters are added with filters:{}".format(appName, len(listForAddedFilterNames), listForAddedFilterNames))
  
  #app.run(host="0.0.0.0", port=thisPortNumber, debug=True)
  #app.run(host=serviceIpAddress, port=thisPortNumber)

  logDebug("appName:[{}]\tdebugMode:[{}], sslMode:[{}]".format(appName, debugMode, sslMode))
  if sslMode:
    try:
      app.run(host=serviceIpAddress, port=thisPortNumber, debug=debugMode, ssl_context=(join(appPath, "cert_{}.pem".format(appName)), join(appPath, "key_{}.pem".format(appName))))
    except:
      logException("appName:[{}]\tfailed to start with the ssl certificate".format(appName))
      app.run(host=serviceIpAddress, port=thisPortNumber, debug=debugMode, ssl_context="adhoc")
  else:  
    app.run(host=serviceIpAddress, port=thisPortNumber, debug=debugMode)
