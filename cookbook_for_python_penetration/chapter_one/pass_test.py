#!/usr/bin/python
import crypt
import time


def decryption(filename,dictionary):
  try:
    with open(filename,'r') as f:
      for line in f:
        shadow = line.strip('\n')
        user = shadow.split(":")[0]
        cryptpwd = shadow.split(":")[1]
        start = shadow.find('$')
        end = shadow.rfind('$')
        salt = shadow[start:end+1]
        for word in dictionary:
          password = crypt.crypt(word,salt)
          if(password == cryptpwd):
            print("[+]" + user + ": " + word)
  except:
    raise

def main():
  start = time.time()

  dictionary = []
  try:
    with open('dictionary') as f:
      for line in f:
        dictionary.append(line.strip('\n'))
  except:
    raise
  # dictionary = ['1','password','123','egg','ybcase@zyj']
  filename = 'shadow'
  decryption(filename,dictionary)
  # print(dictionary)

  end = time.time()
  print(end - start)

if __name__ == '__main__':
  main()
