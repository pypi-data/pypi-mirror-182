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

import os
from os.path import expanduser

import subprocess
import shlex

setLogLevel("DEBUG")
# https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

def create(certName, expirationDays, countryName, stateOrProvinceName, localityName, organizationName, organizationalUnitName, serverFQDNOrYourName, emailAddress, dirPath = "./"):
  currentWorkingDirectory = os.getcwd()
  os.chdir(expanduser(dirPath))
  logDebug("currentWorkingDirectory:[{}]->[{}]".format(currentWorkingDirectory, os.getcwd()))
  
  openSSLCertificateInformation = """US
Washington
Seattle
GraphCode
GC
GraphCode
cert@graphcode.io
"""

  encodedOpenSSLCertificateInformation = """{}
{}
{}
{}
{}
{}
{}
""".format(countryName, stateOrProvinceName, localityName, organizationName, organizationalUnitName, serverFQDNOrYourName, emailAddress).encode()
 
  logDebug("encodedOpenSSLCertificateInformation:[{}]".format(encodedOpenSSLCertificateInformation))
  
  commandLine = "openssl req -x509 -newkey rsa:4096 -nodes -out cert_{}.pem -keyout key_{}.pem -days {}".format(certName, certName, expirationDays)

  resultOfCommand = subprocess.run(shlex.split(commandLine), input=encodedOpenSSLCertificateInformation)
  print()
  
  os.chdir(currentWorkingDirectory)
  logDebug("currentWorkingDirectory:[{}]".format(os.getcwd()))
  
  return resultOfCommand

if __name__ == "__main__":

  resultOfCommand = create(
    certName="graphcode",
    expirationDays=365, 
    countryName="US", 
    stateOrProvinceName="Washington", 
    localityName="Seattle", 
    organizationName="GraphCode", 
    organizationalUnitName="GCD", 
    serverFQDNOrYourName="GraphCode", 
    emailAddress="cert@graphcode.io")
  
  logDebug(resultOfCommand)
  