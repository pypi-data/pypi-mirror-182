'''
The License For Peaceful Use

Copyright (c) 2017-2217 Ryeojin Moon
Copyright (c) 2020-3333 GraphCode

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
WHO HAVE OWNED THE COPYRIGHT OF THIS SOFTWARE.
===
Created by January 1st, 2017
Revised on January 1st, 2017 by @author: ryeojin1@gmail.com
'''
from os.path import join, dirname

def version():
  return "0.1.4.13"


def version2():
  filenameForVersion = join(dirname(__file__), "VERSION")
  f = open(filenameForVersion, "r")
  thisVersion = f.readline()
  f.close()
  
  return thisVersion