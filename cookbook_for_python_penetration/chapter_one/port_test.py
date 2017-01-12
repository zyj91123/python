#!/usr/bin/python
import socket
import os
import sys

def retBanner(ip,port):
  try:
    # print('ip:'+ip+' port:'+str(port))
    socket.setdefaulttimeout(2)
    s = socket.socket()
    s.connect((ip,port))
    banner = s.recv(1024)
    return banner
  except Exception as e:
    # print("[-] Error: "+str(e))
    return

def checkVulns(banner,filename):
  banner = banner.decode()
  with open(filename,'r') as f:
    for line in f:
      # print(line)
      if line.strip('\n') in banner:
        print('   [+] Server is vulnerable: ' + banner.strip('\n'))

def main():
  # filename = 'vlu-banners'
  if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
      print('[-]' + filename + 'does not exist.')
      exit(0)
    if not os.access(filename,os.R_OK):
      print('[-]' + filename + 'access denied.')
      exit(0)
    else:
      print('[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
      # exit(0)
      portlist = [21,22,25,80,110,443]
      for x in range (50,60):
        ip = '10.21.168.' + str(x)
        for port in portlist:
          banner = retBanner(ip,port)
          if banner:
            print('[+] ' + ip + ': ' + str(banner))
            checkVulns(banner,filename)

if __name__=='__main__':
  main()
