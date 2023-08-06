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

from os.path import split

def loadDirAsModule(dirpath):
  #logDebug("#dirpath:[{}]".format(dirpath))
  
  dir_list = split(dirpath)
  if len(dir_list) > 0:
    try:
      __import__(dir_list[-1], fromlist=[''])
      logDebug("module:[{}] is loaded".format(dir_list[-1]))
      return dir_list[-1]
    except:
      logError("unable to load module:[{}]".format(dir_list[-1]))
      loadedModuleName = loadDirAsModule(dir_list[0])
      
      return "{}.{}".format(loadedModuleName, dir_list[-1])
      
  else:
    raiseValueError("unable to split dirpath:[{}]".format(dirpath))
   
def isNamingForApps(name):
  if name[0].lower() >= 'a' and name[0].lower() <= 'z':
    if len(name) > 1:
      for charOffset in range(1,len(name)):
        if (name[charOffset].lower() >= 'a' and name[charOffset].lower() <= 'z') or (name[charOffset].lower() >= '0' and name[charOffset].lower() <= '9'):
          return True
        else:
          raiseValueError("name:[{}] must be alphabets or number")
    else:
      return True
  else:
    raiseValueError("name:[{}] must be started with an alphabet")
    
def isNamingForAction(name):
  if (name[0].lower() >= 'a' and name[0].lower() <= 'z') or (name[0].lower() >= '0' and name[0].lower() <= '9'):
    if len(name) > 1:
      for charOffset in range(1,len(name)):
        if (name[charOffset].lower() >= 'a' and name[charOffset].lower() <= 'z') or (name[charOffset].lower() >= '0' and name[charOffset].lower() <= '9'):
          return True
        else:
          raiseValueError("name:[{}] must be alphabets or number")
    else:
      return True
  else:
    raiseValueError("name:[{}] must be started with an alphabet")
    
def isValidTcpPortNumber(portNumber):
  if isinstance(portNumber, int) and (portNumber > 1 and portNumber < 65536):
    return True
  else:
    raiseValueError("portNumber:[{}] must be integer, greater than 1 and less than 65536".format(portNumber))

def isValidHttpRequest(httpRequest):
  if httpRequest.upper() in ["CONNECT","DELETE","GET","HEAD","OPTIONS","POST","PUT","TRACE"]:
    return True
  else:
    raiseValueError("http request:[{}] is not supported".format(httpRequest))

def isValidHttpFormat(httpRequest):
  if httpRequest.upper() in ["HTML","JSON"]:
    return True
  else:
    raiseValueError("http request:[{}] is not supported".format(httpRequest))
    
def getKwargs(**kwargs):
  name = kwargs["name"]
  try:
    value = kwargs["value"]
  except:
    value = None
    #logWarn("value:[{}] is set".format(value))
  
  dictForKwargs = kwargs["kwargs"]
           
  try:
    #logDebug("#name:[{}]->value:[{}]".format(name, dictForKwargs[name]))
    return dictForKwargs[name]
  except:
    #logDebug("#name:[{}]->value:[{}]".format(name, value))
    return value
