#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
import time
from threading import Thread

def parser(url):
  start = time.time()
  user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'
  headers = { 'User-Agent' : user_agent }
  try:
      request = urllib2.Request(url,headers = headers)
      response = urllib2.urlopen(request)
      opent = time.time()
      print "open: "+str(opent-start)
      content = response.read()
      readt = time.time()
      print "read: "+str(readt-opent)
      # print len(content)

      pt = '<a.*?href="(.*?)"'                               #连接
      pattern = re.compile(pt,re.S)
      items = re.findall(pattern,content)
      items = list(set(items))
      for item in items:
        if(re.match('https://movie.douban.com/subject/.*?',item)):
          print item
      end = time.time()
      print "proc: "+str(end-readt)
      print "---------------------------"
  except urllib2.URLError, e:
      if hasattr(e,"code"):
          print e.code
      if hasattr(e,"reason"):
          print e.reason

# def saveToMysql():
#   pass

def main():
  # start = time.time()
  urllist = []
  urllist.append('https://movie.douban.com/tag/2011')

  for url in urllist:
    t = Thread(target=parser,args=(url,))
    t.start()

  # end = time.time()
  # print "total: "+str(end-start)

if __name__ == '__main__':
  main()
