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

def response(**kwargs):
  dictForResponse = getKwargs(name="dictForResponse", kwargs=kwargs)
  dictForResponseMetadata = getKwargs(name="dictForResponseMetadata", kwargs=kwargs)
  dictForHttpMetadata = getKwargs(name="dictForHttpMetadata", kwargs=kwargs)
  
  htmlForDebugInformation = ""
    
  listForHtmlForResponse = []
  listForHtmlForResponse.append("<p>Response</p>")
  listForHtmlForResponse.append("<ul>")
  for thisKey in dictForResponse.keys():
    listForHtmlForResponse.append("<li><b>{}</b>:{}</li>".format(thisKey, dictForResponse[thisKey]))
  listForHtmlForResponse.append("</ul>")
  
  for htmlLine in listForHtmlForResponse:
    htmlForDebugInformation += "{}\n".format(htmlLine)
  
  listForHtmlForResponseMetadata = []
  listForHtmlForResponseMetadata.append("<p>ResponseMetadata</p>")
  listForHtmlForResponseMetadata.append("<ul>")
  for thisKey in dictForResponseMetadata.keys():
    listForHtmlForResponseMetadata.append("<li><b>{}</b>:{}</li>".format(thisKey, dictForResponseMetadata[thisKey]))
  listForHtmlForResponseMetadata.append("</ul>")
  
  for htmlLine in listForHtmlForResponseMetadata:
    htmlForDebugInformation += "{}\n".format(htmlLine)

  listForHtmlForHttpMetadata = []
  listForHtmlForHttpMetadata.append("<p>HttpMetadata</p>")
  listForHtmlForHttpMetadata.append("<ul>")
  for thisKey in dictForHttpMetadata.keys():
    listForHtmlForHttpMetadata.append("<li><b>{}</b>:{}</li>".format(thisKey, dictForHttpMetadata[thisKey]))
  listForHtmlForHttpMetadata.append("</ul>")
  
  for htmlLine in listForHtmlForHttpMetadata:
    htmlForDebugInformation += "{}\n".format(htmlLine)
    
  return htmlForDebugInformation
    
