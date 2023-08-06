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
from graphcode.logging import logDebug, logInfo, logError, raiseValueError, logWarn, logCritical, logException, logExceptionWithValueError

from graphcode.path import getWorkDirname

from os import mkdir
from os.path import expanduser, join, exists

import json

def getDefaultConf():
  return {
    "service":"~/.graphcode/conf/service.json",
    "coreFrame":"~/.graphcode/conf/ux/frame.json",
    "coreCSS":"~/.graphcode/conf/ux/css.json",
    "coreJS":"~/.graphcode/conf/ux/js.json",
    "coreModal":"~/.graphcode/conf/ux/modal.json",
    "topNav":"~/.graphcode/conf/nav/top.json",
    "leftNav":"~/.graphcode/conf/nav/left.json",
    "rightNav":"~/.graphcode/conf/nav/right.json",
    "bottomNav":"~/.graphcode/conf/nav/bottom.json",
    "static":"static",
    "templates":"templates",
    "rules":"rules",
  }
  
def load(homeDir = "~/"):
  filenameForGraphCodeConf = expanduser(join(homeDir, ".graphcode/conf/graphcode.conf"))
  logDebug("filenameForGraphCodeConf:[{}]".format(filenameForGraphCodeConf))
  
  try:
    f = open(filenameForGraphCodeConf, "r")
    dictForGraphCodeConf = json.load(f)
    f.close()
    
    logInfo("'dictForGraphCodeConf' is loaded from filenameForGraphCodeConf:[{}]".format(filenameForGraphCodeConf))
    for key in dictForGraphCodeConf.keys():
      logDebug("dictForGraphCodeConf\t{}:[{}]".format(key, dictForGraphCodeConf[key]))
      
    return dictForGraphCodeConf
  
  except:
    logException("failed to load filename:[{}]".format(filenameForGraphCodeConf))
    
    homeDirnameForGraphCodeConf = expanduser(join(homeDir, ".graphcode"))
    logDebug("homeDirnameForGraphCodeConf:[{}]".format(homeDirnameForGraphCodeConf))
    if exists(homeDirnameForGraphCodeConf) != True:
      try:
        mkdir(homeDirnameForGraphCodeConf)
        logInfo("homeDirnameForGraphCodeConf:[{}] is created".format(homeDirnameForGraphCodeConf))
      except:
        logExceptionWithValueError("failed to create dirname:[{}]".format(homeDirnameForGraphCodeConf))
    
    confDirnameForGraphCodeConf = join(homeDirnameForGraphCodeConf, "conf")
    logDebug("confDirnameForGraphCodeConf:[{}]".format(confDirnameForGraphCodeConf))
    if exists(confDirnameForGraphCodeConf) != True:
      try:
        mkdir(confDirnameForGraphCodeConf)
        logInfo("confDirnameForGraphCodeConf:[{}] is created".format(confDirnameForGraphCodeConf))
      except:
        logExceptionWithValueError("failed to create dirname:[{}]".format(confDirnameForGraphCodeConf))
  
    try:
      dictForGraphCodeConf = getDefaultConf()
      
      f = open(filenameForGraphCodeConf, "w")
      json.dump(dictForGraphCodeConf, f)
      f.close()
      
      logInfo("'dictForGraphCodeConf' is stored at filenameForGraphCodeConf:[{}]".format(filenameForGraphCodeConf))
      for key in dictForGraphCodeConf.keys():
        logDebug("dictForGraphCodeConf\t{}:[{}]".format(key, dictForGraphCodeConf[key]))
        
        
      return dictForGraphCodeConf
    
    except:
      logExceptionWithValueError("failed to store 'dictForGraphCodeConf' to  filenameForGraphCodeConf:[{}]".format(filenameForGraphCodeConf))
    
    
    