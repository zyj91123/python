#!/usr/bin/python
import zipfile
from threading import Thread
from optparse import OptionParser


def main():
  usage = "usage: %prog -f <zipfile> -d <dictionary>"
  parser = OptionParser(usage)
  parser.add_option("-f","--file",action="store",dest="fname",metavar="FILE",help="specify zip file")
  parser.add_option("-d","--dictionary",action="store",dest="dname",metavar="DICTIONARY",help="specify dictionary file")
  (options, args) = parser.parse_args()
  if(options.fname == None) | (options.dname == None):
    print(parser.usage)
    exit(0)
  else:
    fname = options.fname
    dname = options.dname

if __name__ == '__main__':
  main()
