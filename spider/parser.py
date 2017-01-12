#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
import time
from threading import Thread
# import pymysql

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

      pts = []
      pts.append("<h1>.*?<span.*?>(.*?)</span>")                               #片名
      pts.append("<span.*?year.*?\((.*?)\)</span>")                            #年份
      pts.append("<span.*?类型.*?span>.*?<span.*?>(.*?)</span>")               #类别
      pts.append("<span.*?国家.*?span>(.*?)<br.*?<span.*?语言.*?</span>")      #国家
      pts.append("<strong.*?rating_num.*?>(.*?)</strong>")                     #评分
      tag = ['片名','年份','类别','国家','评分']
      for i in range(len(pts)):
        pattern = re.compile(pts[i],re.S)
        item = re.findall(pattern,content[10000:20000])
        print tag[i]+": "+item[0].strip(' ')
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
  start = time.time()
  urllist = []
  urllist.append('https://movie.douban.com/subject/26416603/')
  urllist.append('https://movie.douban.com/subject/25815034/')
  urllist.append('https://movie.douban.com/subject/26820833/')
  urllist.append('https://movie.douban.com/subject/26932873/')
  urllist.append('https://movie.douban.com/subject/24325861/')

  for url in urllist:
    t = Thread(target=parser,args=(url,))
    time.sleep(0.5)
    t.start()

  end = time.time()
  print "total: "+str(end-start)

if __name__ == '__main__':
  main()
