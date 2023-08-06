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
  
from graphcode.version import version
from graphcode.package import writeVersion

from setuptools import setup, find_packages

from os import remove, symlink
from os.path import dirname, join, expanduser, exists

import shutil

setLogLevel("DEBUG")

PACKAGE_NAME = "graphcode"
writeVersion(packageName=PACKAGE_NAME)
    
VERSION = version()
logInfo("VERSION:[{}]".format(VERSION))

VERSION_list = VERSION.split(".")
try:
  try:
    VERSION_list[-1] = int(VERSION_list[-1]) + 1
  except:
    if chr(ord(VERSION[-1]) + 1).lower() >= 'a' and chr(ord(VERSION[-1]) + 1).lower() <= 'z':
      VERSION[-1] = chr(ord(VERSION[-1]) + 1)
    else:
      VERSION = "{}.gc.1".format(VERSION)
    
  versionNumberOffset = 0
  NEXT_VERSION = ""
  for thisVersion in VERSION_list:
    logDebug("versionNumberOffset:{}:[{}]".format(versionNumberOffset, thisVersion))
    versionNumberOffset += 1
    
    if NEXT_VERSION == "":
      NEXT_VERSION = "{}".format(thisVersion)
      logDebug("NEXT_VERSION:[{}]".format(NEXT_VERSION))  
    else:
      NEXT_VERSION += ".{}".format(thisVersion)
      logDebug("NEXT_VERSION:[{}]".format(NEXT_VERSION))  
    
except:
  logException("unexpected version format:[{}]".format(VERSION))
  NEXT_VERSION = "{}.n.1".format(VERSION)
logDebug("NEXT_VERSION:[{}]".format(NEXT_VERSION))  

targetDirname = dirname(__file__).replace(VERSION, NEXT_VERSION)
logDebug("targetDirname:[{}]".format(targetDirname))
try:
  shutil.copytree(dirname(__file__), targetDirname)
except:
  logException("failed to copy to next version:[{}]".format(NEXT_VERSION))

filenameForTargetProjectXML = join(targetDirname, ".project")
f = open(filenameForTargetProjectXML, "r")
xmlForTargetProject = f.read().replace(VERSION, NEXT_VERSION)
logDebug("xmlForTargetProject:\n===\n{}\n===".format(xmlForTargetProject))
f.close()

f = open(join(targetDirname, ".project"), "w")
f.write(xmlForTargetProject)
logDebug("filenameForTargetProjectXML:[{}] is written completely".format(filenameForTargetProjectXML))
f.close()

dirnameForLinkedTargetDirname = join(expanduser("~/"),"graphcode")
if exists(dirnameForLinkedTargetDirname):
  remove(dirnameForLinkedTargetDirname)
  logDebug("dirname:[{}] is removed".format(join(expanduser("~/"),"graphcode")))

symlink(targetDirname, join(expanduser("~/"),"graphcode"))
logDebug(" a symbolic link:[{}] is created pointing to targetDirname:[{}]".format(join(expanduser("~/"),"graphcode"), targetDirname))

DESCRIPTION = 'A foundation package to enable builders developing web services'
LONG_DESCRIPTION = 'A foundation package to enable builders developing web services'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="graphcode", 
        version=VERSION,
        author="Ryeojin Moon",
        author_email="<ryeojin1@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        python_requires=">=3.10",
        install_requires=["boto3>=1.26.22"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        package_data={
          "graphcode": ["LICENSE", "VERSION"]
        },
        
        keywords=['graphcode', 'web service', 'web services', 'cloud', 'aws', 'azure', 'gcp', 'google cloud'],
        classifiers= [
            "License :: Free To Use But Restricted",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
        ]
)

  


