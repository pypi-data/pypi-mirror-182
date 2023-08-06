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
import sys
import inspect

import platform

from os import mkdir, getpid, getppid, environ
from os.path import abspath, exists, expanduser, join, dirname

import time
from pytz import timezone
from datetime import datetime

import logging

__DEFAULT_LOGLEVEL__ = "DEBUG"

def logMsg(msg):
  countI = 0
  for stackItem_list in inspect.stack():
    if stackItem_list[3] != "logInfo" \
        and stackItem_list[3] != "logError" \
        and stackItem_list[3] != "logTrace" \
        and stackItem_list[3] != "logUnitTest" \
        and stackItem_list[3] != "logDebug" \
        and stackItem_list[3] != "logMsg" \
        and stackItem_list[3] != "logException" \
        and stackItem_list[3] != "logMsgForException"\
        and stackItem_list[3] != "logExceptionWithValueError" \
        and stackItem_list[3] != "logWarn" \
        and stackItem_list[3] != "logCritical" \
        and stackItem_list[3] != "loadJson" \
        and stackItem_list[3] != "getItem" \
        and stackItem_list[3] != "putItemW" \
        and stackItem_list[3] != "deleteItem" \
        and stackItem_list[3] != "getItemWithS3" \
        and stackItem_list[3] != "putItemWithS3" \
        and stackItem_list[3] != "deleteItemWithS3" :
      break
    #print("{}:[{}]".format(-countI, inspect.stack()[countI][3]))
    countI += 1
  
  try:
    msg = "\t{}:{}\t{}:{}:{}->{}:{}:{}\t{}".format(
                                   getppid(), 
                                   getpid(),
                                   inspect.stack()[countI+1][1][len(abspath("."))+1:],inspect.stack()[countI+1][2], inspect.stack()[countI+1][3],
                                   inspect.stack()[countI][1][len(abspath("."))+1:],inspect.stack()[countI][2], inspect.stack()[countI][3],
                                   msg)
  except:
    msg = "\t{}:{}\t{}:{}:{}\t{}".format(
                                   getppid(), 
                                   getpid(),
                                   inspect.stack()[countI][1][len(abspath("."))+1:],inspect.stack()[countI][2], inspect.stack()[countI][3],
                                   msg)
    
  return msg


def logMsgForException(msg = None):
  exc_type, exc_obj, tb = sys.exc_info()
  f = tb.tb_frame
  lineno = tb.tb_lineno
  filename = f.f_code.co_filename[len(abspath("./"))+1:]
  
  countI = 0
  for stackItem_list in inspect.stack():
    if stackItem_list[3] != "logException" and stackItem_list[3] != "logMsgForException":
      break
    #print("{}:[{}]".format(-countI, inspect.stack()[countI][3]))
    countI += 1
  
  if msg == None:
    try:
      msg = "\t{}:{}\t{}:{}:{}->{}:{}:{}\tEXCEPTION IN ({}) \"{}\"".format(
                                                    getppid(), 
                                                    getpid(),
                                                    inspect.stack()[countI+1][1][len(abspath("."))+1:],inspect.stack()[countI+1][2], inspect.stack()[countI+1][3],
                                                    filename, lineno, inspect.stack()[countI][3],
                                                    exc_type, exc_obj
                                                    )
    except:
      msg = "\t{}:{}\t{}:{}:{}\tEXCEPTION IN ({}) \"{}\"".format(
                                                    getppid(), 
                                                    getpid(),
                                                    filename, lineno, inspect.stack()[countI][3],
                                                    exc_type, exc_obj
                                                    )
      
  else:
    try:
      msg = "\t{}:{}\t{}:{}:{}->{}:{}:{}\tEXCEPTION IN ({}) \"{}\" -> Error:[{}]".format(
                                                  getppid(), 
                                                  getpid(),
                                                  inspect.stack()[countI+1][1][len(abspath("."))+1:],inspect.stack()[countI+1][2], inspect.stack()[countI+1][3],
                                                  filename, lineno, inspect.stack()[countI][3],
                                                  exc_type, exc_obj,
                                                  msg
                                                  )
    except:
      msg = "\t{}:{}\t{}:{}:{}\tEXCEPTION IN ({}) \"{}\" -> Error:[{}]".format(
                                                  getppid(), 
                                                  getpid(),
                                                  filename, lineno, inspect.stack()[countI][3],
                                                  exc_type, exc_obj,
                                                  msg
                                                  )
  return msg

def getLogPriorityNumber(logLevel):
  if logLevel == "DEBUG":
    logPriorityNumber = logging.DEBUG
  elif logLevel == "INFO":
    logPriorityNumber = logging.INFO
  elif logLevel == "WARN":
    logPriorityNumber = logging.WARN
  elif logLevel == "ERROR":
    logPriorityNumber = logging.ERROR
  elif logLevel == "CRITICAL":
    logPriorityNumber = logging.CRITICAL
  else:
    logPriorityNumber = logging.INFO
    
  return logPriorityNumber

def setLogLevel(logLevel):
  logPriorityNumber = getLogPriorityNumber(logLevel.upper())
  
  logging.getLogger().setLevel(logPriorityNumber)
  
  logInfo("logLevel:[{}]({}) is set".format(logLevel, logging.getLogger().level))

  try:
    filenameForLogLevel = join(dirname(logging.getLogger().handlers[0].baseFilename).replace("log","pid"), "graphcode-loglevel-{}.log".format(getpid()))
    f = open(filenameForLogLevel, "w")
    logLevel = f.write(logLevel)
    f.close()
    pass#print(logMsg("logLevel:[{}] is stored to '{}'".format(logLevel, filenameForLogLevel)))
  except:
    logMsgForException("logLevel:[{}] is stored to '{}'".format(logLevel, filenameForLogLevel))
    
def getLogLevel():
  logLevel_dict = {
    logging.DEBUG:"DEBUG",
    logging.INFO:"INFO",
    logging.WARN:"WARN",
    logging.ERROR:"ERROR",
    logging.CRITICAL:"CRITICAL",
    }
    
  return logLevel_dict[logging.getLogger().getEffectiveLevel()]

def getLogFilename():
  return logging.getLogger().handlers[0].baseFilename

def initLog():
  pass#print("[~/]:[{}]".format(expanduser("~/")))

  platformInfo = platform.uname()
  pass#print(logMsg("[{}]/[{}]/[{}]/[{}]\tPython Version:[{}]".format(platformInfo.node,  platformInfo.system, platformInfo.release, platformInfo.version, sys.version)))
  
  if platform.system().startswith("Win"):
    tmpDir = expanduser("~\AppData\Local\Temp")
  else:
    tmpDir = expanduser("~/tmp")
    
  pass#print(logMsg("temporary directory:[{}]:[{}]".format(platformInfo.node, tmpDir)))
  
  pass#print(logMsg("ppid:[{}]->pid:[{}]".format(getppid(), getpid())))
  
  if exists(tmpDir):
    pass#print(logMsg("tmpDir:[{}] is already created".format(tmpDir)))
  else:
    try:
      mkdir(tmpDir)
      pass#print(logMsg("tmpDir:[{}] is created".format(tmpDir)))
    except Exception as e:
      errMsg = "Error:[{}]->failed to create tmpDir:[{}]".format(e, tmpDir)
      print(logMsg(errMsg))
      raise ValueError(errMsg)
  
  logDir = join(tmpDir, "log")
  if exists(logDir):
    pass#print(logMsg("logDir:[{}] is already created".format(logDir)))
  else:
    try:
      mkdir(logDir)
      pass#print(logMsg("logDir:[{}] is created".format(logDir)))
    except Exception as e:
      errMsg = "Error:[{}]->failed to create logDir:[{}]".format(e, logDir)
      print(logMsg(errMsg))
      raise ValueError(errMsg)
  
  pidDir = join(tmpDir, "pid")
  if exists(pidDir):
    pass#print(logMsg("pidDir:[{}] is already created".format(pidDir)))
  else:
    try:
      mkdir(pidDir)
      pass#print(logMsg("pidDir:[{}] is created".format(pidDir)))
    except Exception as e:
      errMsg = "Error:[{}]->failed to create pidDir:[{}]".format(e, pidDir)
      print(logMsg(errMsg))
      raise ValueError(errMsg)
  
  filenameForLogFilename = join(pidDir, "graphcode-{}.log".format(getppid()))
  pass#print(logMsg("filenameForLogFilename:[{}] is set".format(filenameForLogFilename)))
  try:
    f = open(filenameForLogFilename, "r")
    logFilename = f.readline()
    f.close()
    pass#print(logMsg("logFilename:[{}] is loaded from '{}'".format(logFilename, filenameForLogFilename)))
    
    thisLogFilenameStoredFilename = join(pidDir, "graphcode-{}.log".format(getpid()))
    pass#print(logMsg("thisLogFilenameStoredFilename:[{}]".format(thisLogFilenameStoredFilename)))
    f = open(thisLogFilenameStoredFilename, "w")
    f.write(logFilename)
    f.close()
    pass#print(logMsg("logFilename:[{}] is saved at '{}'".format(logFilename, thisLogFilenameStoredFilename)))
    
  except:
    logFileTimestamp = datetime.fromtimestamp(time.time()).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H-%M-%S_%f%Z')
    logFilename = join(logDir, "graphcode-{}.log".format(logFileTimestamp))
    pass#print(logMsg("logFilename:[{}] is to be stored at filenameForLogFilename:[{}]".format(logFilename, filenameForLogFilename)))
  
    try:
      f = open(filenameForLogFilename, "w")
      f.write(logFilename)
      f.close()
      pass#print(logMsg("logFilename:[{}] is stored at filenameForLogFilename:[{}] sucessfully".format(logFilename, filenameForLogFilename)))
    except:
      print(logMsgForException("failed to store logFilename:[{}] at filenameForLogFilename:[{}]".format(logFilename, filenameForLogFilename)))
  pass#print(logMsg("logFilename:[{}]".format(logFilename)))
  
  filenameForLogLevel = join(pidDir, "graphcode-loglevel-{}.log".format(getppid()))
  try:
    f = open(filenameForLogLevel, "r")
    logLevel = f.readline()
    f.close()
    pass#print(logMsg("logLevel:[{}] is loaded from '{}'".format(logLevel, filenameForLogLevel)))
  except:
    logLevel = __DEFAULT_LOGLEVEL__
    pass#print(log("logLevel:[{}] is set from __DEFAULT_LOGLEVEL__:[{}]".format(logLevel, __DEFAULT_LOGLEVEL__)))
  
    filenameForLogLevel = join(pidDir, "graphcode-loglevel-{}.log".format(getpid()))
    try:
      f = open(filenameForLogLevel, "w")
      logLevel = f.write(logLevel)
      f.close()
      pass#print(logMsg("logLevel:[{}] is stored to '{}'".format(logLevel, filenameForLogLevel)))
    except:
      logMsgForException("logLevel:[{}] is stored to '{}'".format(logLevel, filenameForLogLevel))
  
  logPriorityNumber = getLogPriorityNumber(logLevel)
  logging.basicConfig(
    handlers=[
        logging.FileHandler(logFilename),
        logging.StreamHandler()
    ],
    format='%(asctime)s %(levelname)s %(message)s', 
    datefmt='%m/%d/%Y %H:%M:%S UTC',
    level=logPriorityNumber)
  
  logInfo("logging is initialized with filename:[{}](level:{}:{})".format(logFilename, logLevel, logging.getLogger().level))

def rotateLogfile(logLevel = None):
  logDir = dirname(logging.getLogger().handlers[0].baseFilename)
  pidDir = logDir.replace("log","pid")
  
  logFileTimestamp = datetime.fromtimestamp(time.time()).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H-%M-%S_%f%Z')
  logFilename = join(logDir, "graphcode-{}.log".format(logFileTimestamp))
  pass#print(logMsg("logFilename:[{}] is to be stored at filenameForLogFilename:[{}]".format(logFilename, filenameForLogFilename)))
  
  filenameForLogFilename = join(pidDir, "graphcode-{}.log".format(getppid()))
  try:
    f = open(filenameForLogFilename, "w")
    f.write(logFilename)
    f.close()
    pass#print(logMsg("logFilename:[{}] is stored at filenameForLogFilename:[{}] sucessfully".format(logFilename, filenameForLogFilename)))
  except:
    print(logMsgForException("failed to store logFilename:[{}] at filenameForLogFilename:[{}]".format(logFilename, filenameForLogFilename)))

  if logLevel == None:
    filenameForLogLevel = join(pidDir, "graphcode-loglevel-{}.log".format(getppid()))
    try:
      f = open(filenameForLogLevel, "r")
      logLevel = f.readline()
      f.close()
      pass#print(logMsg("logLevel:[{}] is loaded from '{}'".format(logLevel, filenameForLogLevel)))
    except:
      logLevel = __DEFAULT_LOGLEVEL__
      pass#print(log("logLevel:[{}] is set from __DEFAULT_LOGLEVEL__:[{}]".format(logLevel, __DEFAULT_LOGLEVEL__)))
    
      filenameForLogLevel = join(pidDir, "graphcode-loglevel-{}.log".format(getpid()))
      try:
        f = open(filenameForLogLevel, "w")
        logLevel = f.write(logLevel)
        f.close()
        pass#print(logMsg("logLevel:[{}] is stored to '{}'".format(logLevel, filenameForLogLevel)))
      except:
        logMsgForException("logLevel:[{}] is stored to '{}'".format(logLevel, filenameForLogLevel))
  else:
    setLogLevel(logLevel)
    
  logPriorityNumber = getLogPriorityNumber(logLevel)
  logging.basicConfig(
    handlers=[
        logging.FileHandler(logFilename),
        logging.StreamHandler()
    ],
    format='%(asctime)s %(levelname)s %(message)s', 
    datefmt='%m/%d/%Y %H:%M:%S UTC',
    level=logPriorityNumber)
  
  logInfo("logging is rotated with filename:[{}](level:{}:{})".format(logFilename, logLevel, logging.getLogger().level))

def logDebug(msg):
  logging.debug(logMsg(msg))
  
  return msg
  
def logInfo(msg):
  logging.info(logMsg(msg))
  
  return msg
  
def logWarn(msg):
  logging.warn(logMsg(msg))
  
  return msg
  
def logError(msg):
  logging.error(logMsg(msg))
  
  return msg

def raiseValueError(msg):
  logging.error(logMsg(msg))
  raise ValueError(msg)

def logException(msg = ""):
  errMsg = logMsgForException(msg)
  logging.exception(errMsg)
  
  return errMsg

def logExceptionWithValueError(msg = ""):
  errMsg = logMsgForException(msg)
  logging.exception(errMsg)
  raise ValueError(errMsg)

def logCritical(msg):
  logging.critical(logMsg(msg))
  
  return msg
