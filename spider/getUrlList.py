#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
import time
from threading import Thread

def generateMovieURL(url,urllist):
  start = time.time()
  user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'
  headers = { 'User-Agent' : user_agent }
  try:
      print url
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
          # urllist.append(item)
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

def generateUrlFormYear(year,pageNum,pageList):
  for i in range(pageNum):
    url = 'https://movie.douban.com/tag/'+str(year)+'?start='+str(i*20)+"&type=T"
    pageList.append(url)

def main():
  # start = time.time()
  yearPage = {"2011":66,"2012":78,"2013":88,"2014":105,"2015":148,"2016":324}
  pageList = [] #豆瓣电影每个页面有20部电影，这里生成所有页面
  for year,pageNum in yearPage.items():
    generateUrlFormYear(year,pageNum,pageList)
  # print len(pageList)
  urlList = []
  for url in pageList[0:1]:
    t = Thread(target=generateMovieURL,args=(url,urlList))
    t.start()
    time.sleep(1)
  for i in range(len(urlList)):
    print str(i)+": "+url
  # end = time.time()
  # print "total: "+str(end-start)

if __name__ == '__main__':
  main()
