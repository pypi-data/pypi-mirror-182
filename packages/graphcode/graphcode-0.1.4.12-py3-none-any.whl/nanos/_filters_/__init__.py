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

import json

def dollar(value):
  if isinstance(value, int) or isinstance(value, float):
    return "${:,}".format(value)
  else:
    return "${}".format(value)
  
def usdollar(value):
  if isinstance(value, float):
    if value > 1000000:
      return "${:,.2f}M".format(value/1000000)
    elif value > 1000:
      return "${:,.2f}K".format(value/1000)
    else:
      return "${:,.2f}".format(value)
  elif isinstance(value, int):
    if value > 1000000:
      return "${:,.2f}M".format(value/1000000)
    elif value > 1000:
      return "${:,.2f}K".format(value/1000)
    else:
      return "${:,}".format(value)
  else:
    return value

def usdollar12m(value):
  if isinstance(value, float):
    if value*12 > 1000000:
      return "${:,.2f}M".format(value*12/1000000)
    elif value*12 > 1000:
      return "${:,.2f}K".format(value*12/1000)
    else:
      return "${:,.2f}".format(value*12)
  else:
    return value*12

def number(value):
  if isinstance(value, float):
    return "{:,.2f}".format(value)
  elif isinstance(value, int):
    return "{:,}".format(value)
  else:
    return value
  
def percentage(value):
  if isinstance(value, float):
    return "{:,.2f}%".format(value)
  elif isinstance(value, int):
    return "{:,}%".format(value)
  else:
    return value
  
def length25000(value):
  if isinstance(value, list):
    if len(value) > 25000:
      return value[:25000]
    else:
      return value
  elif isinstance(value, dict):
    if len(value.keys()) > 25000:
      thisValue_dict = {}
      thisItemCount = 0
      for thisKey in thisValue_dict.keys():
        thisValue_dict[thisKey] = thisValue_dict[thisKey]
      
      thisItemCount += 1
      if thisItemCount > 25000:
        return thisValue_dict
    else:
      return value
  else:
    return value

def iterate(value):
  resultTag = ""
  try:
    if isinstance(value, dict):
      for key in value.keys():
        if key in ["outputs", "charts"]:
          resultTag += "<b>{}</b>:<br>".format(key)
          for key2 in value[key].keys():
            if key2 in ["wbResults", "charts"]:
              resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:<br>".format(key2)
            
            elif isinstance(value[key][key2], dict):
              resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:<br>".format(key2)
              for key3 in value[key][key2].keys():
                resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:{}<br>".format(key3, value[key][key2][key3])
            else:
              resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:{}<br>".format(key2, value[key][key2])
        elif key in ["profileSelect"]:
          resultTag += "<b>{}</b>:<br>".format(key)
          for key2 in value[key].keys():
            resultTag += "&nbsp;&nbsp;&nbsp;&nbsp;<b>{}</b>:<br>".format(key2, len(value[key][key2]))
            
        elif key in ["jsCharts"]:
          resultTag += "<b>{}</b>:len:{:,}<br>".format(key, len(value[key]))
        else:
          resultTag += "<b>{}</b>:{}<br>".format(key, value[key])
    else:
      resultTag = json.dump(value)
  except Exception as e:
    resultTag =  logException("Error:[{}]->unable to unpack value:[{}]".format(e, value))
  
  if len(resultTag) > 25000:
    resultTag = "size:{:,}Bytes<br>displaying the first 25K in the value:<br>{}..........{}".format(len(resultTag),resultTag[:25000],resultTag[-1000:])
    
  return resultTag
