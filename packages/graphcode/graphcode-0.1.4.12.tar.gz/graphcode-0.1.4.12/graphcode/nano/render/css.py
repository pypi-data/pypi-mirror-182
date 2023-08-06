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
'''
from graphcode.logging import setLogLevel, logDebug, logInfo, logError, raiseValueError, logWarn, logCritical, logException, logExceptionWithValueError

from graphcode.path import listDir

from graphcode.lib import getKwargs

from os import mkdir, rename
from os.path import join, exists

import time
from pytz import timezone
from datetime import datetime

from shutil import copytree

def generate(**kwargs):
  appPath = getKwargs(name="appPath", kwargs=kwargs)
  logDebug("#appPath:[{}]".format(appPath))
  
  ruleDirname = getKwargs(name="ruleDirname", kwargs=kwargs)
  ruleName = ruleDirname.split("__")[0]
  logDebug("#ruleDirname:[{}]->ruleName:[{}]".format(ruleDirname, ruleName))
  
  themeName = getKwargs(name="themeName", value="default", kwargs=kwargs)
  logDebug("#themeName:[{}]".format(themeName))
 
  htmlTag = "\n<!-- Begin: style sheets for {} -->\n".format(ruleName)
  
  for filename in listDir(dirPath=join(appPath, "_static_", themeName, "_css_"), type="file"):
    if filename.split(".")[-1] in ["css"]:
      htmlTag += "  <link href=\"_static_/{}/_css_/{}\" rel=\"stylesheet\" type=\"text/css\">\n".format(themeName, filename)
  
  if exists(join(appPath, "_static_", "_css_")):
    pass#logDebug("dirName:[{}] is found".format(join(appPath, "_static_", "_css_")))
  else:
    mkdir(join(appPath, "_static_", "_css_"))
    logDebug("dirName:[{}] is created".format(join(appPath, "_static_", "_css_")))
    
  if exists(join(appPath, "_static_", "_css_", ruleName)):
    logWarn("dirname:[{}] may need to be cleaned up to remove the previous style sheets".format(join(appPath, "_static_", "_css_", ruleName)))
    #rename(join(appPath, "_static_", "_css_", ruleName), join(appPath, "_static_", "_css_", "_{}_at_{}".format(ruleName, datetime.fromtimestamp(time.time()).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H-%M-%S_%f%Z'))))
  else: 
    copytree(join(appPath, ruleDirname, "_css_"), join(appPath, "_static_", "_css_", ruleName))
    
  for filename in listDir(dirPath=join(appPath, "_static_", "_css_", ruleName), type="file"):
    if filename.split(".")[-1] in ["css"]:
      htmlTag += "  <link href=\"_static_/_css_/{}/{}\" rel=\"stylesheet\" type=\"text/css\">\n".format(ruleName, filename)
    
  htmlTag += "<!-- End: style sheets for {} -->\n\n".format(ruleName)
  #logDebug(htmlTag)
  return htmlTag