#!/usr/bin/env python
# encoding: utf-8
#
# tf-idf example in Python
# by Tim Trueman provided under:
# 
# The MIT License
# 
# Copyright (c) 2009 Tim Trueman
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php

import math
from operator import itemgetter

def freq(word, document):
  return document.split(None).count(word)

def wordCount(document):
  return len(document.split(None))

def numDocsContaining(word,documentList):
  count = 0
  for document in documentList:
    if freq(word,document) > 0:
      count += 1
  return count

def tf(word, document):
  return (freq(word,document) / float(wordCount(document)))

def idf(word, documentList):
  return math.log(len(documentList) / numDocsContaining(word,documentList))

def tfidf(word, document, documentList):
  return (tf(word,document) * idf(word,documentList))

if __name__ == '__main__':
  documentList = []
  documentList.append("""DOCUMENT #1 TEXT""")
  documentList.append("""DOCUMENT #2 TEXT""")
  documentList.append("""DOCUMENT #3 TEXT""")
  words = {}
  documentNumber = 0
  for word in documentList[documentNumber].split(None):
    words[word] = tfidf(word,documentList[documentNumber],documentList)
  for item in sorted(words.items(), key=itemgetter(1), reverse=True):
    print "%f <= %s" % (item[1], item[0])