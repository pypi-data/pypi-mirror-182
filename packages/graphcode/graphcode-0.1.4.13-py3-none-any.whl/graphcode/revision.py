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

from os import mkdir, getpid, getppid
from os.path import join, dirname, basename, exists


import time
from pytz import timezone
from datetime import datetime

import zipfile
import pathlib

def loadRevision():
  filenameForRevision = join(getWorkDirname(),"REVISION")
  try:
    f = open(filenameForRevision, "r")
    oldRevision = f.readline()
    f.close()
  except:
    logException("failed to read filenameForRevision:[{}]".format(filenameForRevision))
  
    oldRevision = "0.0.{}.0,{},{}".format(datetime.today().year, time.time(),  getpid())
    
  return oldRevision

def getNextRevision():
  oldRevision = loadRevision()
  
  revisionPID = oldRevision.split(",")[-1]
  try:
    lastUpdateDelta = (time.time() - float(oldRevision.split(",")[-2]))
  except:
    logException("failed to set the last update time with oldRevision:[{}]".format(oldRevision))
    lastUpdateDelta = time.time()
    
  if lastUpdateDelta < 30:
    logWarn("revision:[{}] is updated in [{:,.2f}]s ago. ignored!".format(oldRevision.split(",")[0], lastUpdateDelta))  
    
    return oldRevision
  
  else:
    oldRevision_list = oldRevision.split(",")[0].split(".")
    if revisionPID != getppid():
      try:
        oldRevision_list[-1] = int(oldRevision_list[-1]) + 1
        
        revisionNumberOffset = 0
        nextRevision = ""
        for versioNumber in oldRevision_list:
          logDebug("revisionNumberOffset:{}:[{}]".format(revisionNumberOffset, nextRevision))
          revisionNumberOffset += 1
          
          if nextRevision == "":
            nextRevision = "{}".format(versioNumber)
            logDebug("nextRevision:[{}]".format(nextRevision))  
          else:
            nextRevision += ".{}".format(versioNumber)
            logDebug("nextRevision:[{}]".format(nextRevision))  
          
      except:
        logException("unexpected revision format:[{}]".format(oldRevision))
        nextRevision = "{}.n.1".format(oldRevision)
      
      logDebug("nextRevision:[{}]".format(nextRevision))  
      
      return "{},{},{}".format(nextRevision, time.time(), getpid())
  
    else:
      logDebug("revisionPID:[{}] is the ppid:[{}] of the current process:[{}]".format(revisionPID, getppid(), getpid()))
      
      return oldRevision
  

def saveNextRevision():
  
  filenameForRevision = join(getWorkDirname(),"REVISION")
  try:
    nextRevision = getNextRevision()
    
  except:
    logException("failed to saveNextRevision".format(filenameForRevision))
    nextRevision = "0.0.{}.0,{}".format(datetime.today().year, getpid())
  
  f = open(filenameForRevision, "w")
  f.write(nextRevision)
  f.close()
  
  #f = open(filenameForRevision, "r")
  #thisRevision = f.readline()
  #f.close()
  #logDebug("thisRevision:[{}]".format(thisRevision))
  
  return nextRevision.split(",")[0]

def createZipArchive(sourceDir, archiveDir, archiveKey):
  zipFilename = join(archiveDir, archiveKey)
  if exists(zipFilename):
    logDebug("zipFilename:[{}] is already created".format(zipFilename))
  
  else:
    logDebug("zipFilename:[{}] is created".format(zipFilename))
    # zipf is zipfile handle
    zipf = zipfile.ZipFile("{}".format(zipFilename), 'w', zipfile.ZIP_DEFLATED)
    #zipf = zipfile.ZipFile("{}".format(zipFilename), 'w', zipfile.ZIP_LZMA)
    
    compressedFileCount = 0
    directory = pathlib.Path(sourceDir)
    for file_path in directory.rglob("*"):
      if "__pycache__" in "{}".format(file_path):
        pass#logDebug("(#{:,})\tskipped...{}".format(compressedFileCount, file_path ))
      elif ".pyc" == file_path.suffix:
        pass#logDebug("(#{:,})\tskipped...{}".format(compressedFileCount, file_path ))
      else:
        compressedFileCount += 1
        if (compressedFileCount % 2500) == 0:
          logDebug("(#{:,})\t{}".format(compressedFileCount, file_path ))
        zipf.write(file_path, arcname=file_path.relative_to(directory))
    zipf.close()
    logDebug("total {:,} files are compressed to zipFilename:[{}]".format(compressedFileCount, zipFilename))
    
  return zipFilename
  
def revision():
  dirnameForRevision = join(dirname(getWorkDirname().replace(getWorkDirname().split("_")[-1],"")),"revisions")
  logDebug("dirnameForRevision:[{}] is set".format(dirnameForRevision))
  
  if exists(dirnameForRevision):
    logDebug("dirnameForRevision:[{}] is already created".format(dirnameForRevision))
    
  else:
    try:
      mkdir(dirnameForRevision)
      pass#print(logMsg("dirnameForRevision:[{}] is created".format(dirnameForRevision)))
    except:
      logExceptionWithValueError("failed to create dirnameForRevision:[{}]".format(dirnameForRevision))
  
  try:
    archiveKey = "{}(build_{}).zip".format(basename(getWorkDirname()), saveNextRevision())
                   
    return createZipArchive(sourceDir= getWorkDirname(), archiveDir= dirnameForRevision, archiveKey= archiveKey)
  
  except:
    logExceptionWithValueError("failed to revision:[{}]".format(dirnameForRevision))

 
  
  
  
  
  
  
  
  
  
  
  