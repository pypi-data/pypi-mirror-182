'''
The License For Peaceful Use

Copyright (c) 2017-2217 HoeSeong Ha
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

from graphcode.path import listDir, getWorkDirname

from flask import Flask, request, render_template, redirect, url_for

import sys
import inspect
from os import mkdir
from os.path import abspath, dirname, basename, exists, join, split

def loadDirAsModule(dirpath):
  logDebug("dirpath:[{}]".format(dirpath))
  
  dir_list = split(dirpath)
  if len(dir_list) > 0:
    try:
      __import__(dir_list[-1])
      logDebug("module:[{}] is loaded".format(dir_list[-1]))
      return dir_list[-1]
    except:
      logError("unable to load module:[{}]".format(dir_list[-1]))
      loadedModuleName = loadDirAsModule(dir_list[0])
      
      return "{}.{}".format(loadedModuleName, dir_list[-1])
      
  else:
    raiseValueError("unable to split dirpath:[{}]".format(dirpath))
    
  
setLogLevel("DEBUG")

thisName = basename(dirname(__file__)).split("__")[0]
logDebug("thisName:[{}]".format(thisName))

for subDirname in ["_filters_", "_static_", "_templates_"]:
  if join(dirname(__file__), subDirname):
    logDebug("dirname:[{}] is found".format(join(dirname(__file__), subDirname)))
  else:
    mkdir(join(dirname(__file__), subDirname))
    logDebug("dirname:[{}] is created".format(join(dirname(__file__), subDirname)))

# Reference - https://flask.palletsprojects.com/en/2.2.x/api/
app = Flask(
  import_name = thisName,
  static_folder=join(dirname(__file__), "_static_"), 
  template_folder=join(dirname(__file__), "_templates_")
  )

thisParentModuleName = loadDirAsModule(dirpath=dirname(__file__))
logDebug("thisParentModuleName:[{}]".format(thisParentModuleName))
  
for subDirname in listDir(dirPath=dirname(__file__), type = "dir"):
  if subDirname.startswith("__"):
    logDebug("subDirname:[{}] is ignored".format(subDirname))
  else:
    logDebug("subDirname:[{}] is to be added".format(subDirname))
    
    subDirname_list = subDirname.split("__")
    thisRuleName = subDirname_list[0]
    if thisRuleName in ["index"]:
      thisRuleName = "/"
      thisModuleName = "{}.{}".format(thisParentModuleName, subDirname)
    else:
      thisRuleName = "/{}".format(thisRuleName)
      thisModuleName = "{}.{}".format(thisParentModuleName, subDirname)
    
    listForMethods = subDirname_list[-1].split("_")
    logDebug("methods:{}".format(listForMethods))
    try:
      thisSubModule = __import__(thisModuleName, fromlist=[''])
      logDebug("thisModuleName:[{}] is loaded with thisSubModule:[{}]".format(thisModuleName, thisSubModule))
      
      app.add_url_rule(
        rule = thisRuleName, 
        view_func = thisSubModule.view,
        methods=listForMethods
        )
      logInfo("thisRuleName:[{}] is added with view_func:[{}]({})".format(thisRuleName, thisModuleName, thisSubModule))
    
    except:
      logException("unable to load module:[{}]".format(thisModuleName))
  
  break

listForAddedFilterNames = []
try:
  listForParentModuleNames = []
  if len(thisParentModuleName.split(".")) >= 2:
    listForParentModuleNames.append("{}._filters_".format(thisParentModuleName[:-1 - len(thisParentModuleName.split(".")[-1])]))
  listForParentModuleNames.append("{}._filters_".format(thisParentModuleName))
                                   
  for thisParentFilterModuleName in listForParentModuleNames:
    try:
      thisFilterModule = __import__(thisParentFilterModuleName, fromlist=[''])
      logDebug("thisParentFilterModuleName:[{}]->thisFilterModule:[{}] is loaded".format(thisParentFilterModuleName, thisFilterModule.__name__))
      for thisFilterName in dir(thisFilterModule):
        if thisFilterName.startswith("__"):
          logDebug("thisFilterName:[{}] is ignored".format(thisFilterName))
        
        elif basename(dirname(inspect.getfile(getattr(thisFilterModule, thisFilterName)))) == "_filters_":
          if thisFilterName in listForAddedFilterNames:
            logWarn("thisFilterName:[{}] is already added".format(thisFilterName))
          else:
            app.add_template_filter(getattr(thisFilterModule, thisFilterName))
            listForAddedFilterNames.append(thisFilterName)
            logDebug("(#{:,})\tthisParentFilterModuleName:[{}]->thisFilterName:[{}] is added from [{}]".format(len(listForAddedFilterNames), thisParentFilterModuleName, thisFilterName, basename(dirname(inspect.getfile(getattr(thisFilterModule, thisFilterName))))))
            
        else:
          logDebug("thisFilterName:[{}] is ignored".format(thisFilterName))
    except:
      logException("unable to add filters with thisParentFilterModuleName:[{}]".format(thisParentFilterModuleName))  
except:
  logException("[{}._filters_] module failed to load".format(thisParentModuleName))
  
logDebug("total {:,} filters are added with filters:{}".format(len(listForAddedFilterNames), listForAddedFilterNames))

try:
  thisPortNumber=int(split(dirname(__file__))[-1].split("__")[-1])
  logDebug("thisPortNumber:[{}]".format(thisPortNumber))
except:
  raiseValueError("portNumber is not found at dirname:[{}]".format(dirname(__file__)))
  
#app.run(host="0.0.0.0", port=thisPortNumber, debug=True)
app.run(port=thisPortNumber)
