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

from graphcode.lib import getKwargs

from graphcode.nano.response.debug import response as responseForDebug

from os import getppid, getpid

import time
from pytz import timezone
from datetime import datetime

import json
from os.path import dirname, basename, split

from flask import Flask, Response, request, make_response, render_template, redirect, url_for

from uuid import uuid4

def response(**kwargs):
  __beginTime__  = getKwargs(name="__beginTime__", value=time.time(), kwargs=kwargs)
  
  rulePath = getKwargs(name="rulePath", kwargs=kwargs)
  appName = basename(split(dirname(rulePath))[0]).split("__")[0]
  ruleName = split(dirname(rulePath))[-1].split("__")[0]
  requestId  = getKwargs(name="reqeustId", value=uuid4(), kwargs=kwargs)
  httpRequestFormat = getKwargs(name="httpRequestFormat", value="HTML", kwargs=kwargs)
  
  timestamp = datetime.fromtimestamp(__beginTime__).astimezone(timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%S.%f%Z')
  
  dictForResponse = getKwargs(name="dictForResponse", kwargs=kwargs)
  dictForResponseMetadata = {
    "requestId": "{}".format(requestId),
    "appName":appName,
    "ruleName":ruleName,
    "ppid": getppid(),
    "pid": getpid(),
    "rulePath": rulePath,
    "timestamp": timestamp,
    "processTime": time.time() - __beginTime__
    }
  dictForHttpMetadata = {}
  
  if httpRequestFormat in ["HTML"]:
    htmlForDebugInformation = responseForDebug(
      dictForResponse=dictForResponse, 
      dictForResponseMetadata=dictForResponseMetadata, 
      dictForHttpMetadata=dictForHttpMetadata
      )
    
    httpResponse = render_template(
      "{}.html".format(ruleName), 
      debugMode=True,
      debugInformation=htmlForDebugInformation
      )

  elif httpRequestFormat in ["JSON"]:
    httpResponse = Response(
      response=json.dumps(
        {
          "Response":dictForResponse,
          "ResponseMetadata":dictForResponseMetadata,
          "HttpMetadata":dictForHttpMetadata
          }
        ), 
      status=200, 
      mimetype="application/json"
    ) 
    httpResponse.headers['Content-type'] = 'application/json; charset=utf-8'
    
  else:
    httpResponse = "<p>Hello, {}!([{}:{}]{},{})</p>".format(appName, getppid(), getpid(), rulePath, timestamp)
  
  return httpResponse