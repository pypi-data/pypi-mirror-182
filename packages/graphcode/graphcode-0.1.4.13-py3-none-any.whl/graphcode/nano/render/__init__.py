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
Revised on Dec 22, 2022 by @author: ryeojin1@gmail.com
'''
from graphcode.logging import setLogLevel, logDebug, logInfo, logError, raiseValueError, logWarn, logCritical, logException, logExceptionWithValueError

from graphcode.nano.render import css, js

from graphcode.lib import getKwargs

from os.path import split, join, dirname

def render(**kwargs):
  ruleDirname = getKwargs(name="ruleDirname", kwargs=kwargs)
  logDebug("#ruleDirname:[{}]".format(ruleDirname))
  
  appPath = getKwargs(name="appPath", kwargs=kwargs)
  ruleName = ruleDirname.split("__")[0]
  
  listForHtmlForTemplate = []
  listForHtmlForTemplate.append("<html>")
  listForHtmlForTemplate.append("<head>")
  
  listForHtmlForTemplate.append(css.generate(appPath=appPath, ruleDirname=ruleDirname))
  
  listForHtmlForTemplate.append("</head>")
  listForHtmlForTemplate.append("<body>")
  listForHtmlForTemplate.append("<!-- Begin: Body -->")
  listForHtmlForTemplate.append("<!-- End: Body -->")
  listForHtmlForTemplate.append("<!-- Begin: Debug Information -->")
  listForHtmlForTemplate.append("<div>")
  listForHtmlForTemplate.append("{{ debugInformation | safe }}")
  listForHtmlForTemplate.append("</div>")
  listForHtmlForTemplate.append("<!-- End: Debug Information -->")
  
  listForHtmlForTemplate.append(js.generate(appPath=appPath, ruleDirname=ruleDirname))
  
  listForHtmlForTemplate.append("</html>")
  
  htmlForTemplate = ""
  for htmlLine in listForHtmlForTemplate:
    htmlForTemplate += "{}\n".format(htmlLine)
  
  filenameForHtmlTemplate = join(appPath, "_templates_", "{}.html".format(ruleName))
  logDebug("filenameForHtmlTemplate:[{}]".format(filenameForHtmlTemplate))

  f = open(filenameForHtmlTemplate, "w")
  f.write(htmlForTemplate)
  f.close()
  
  return ruleName
  
  
  
  
  