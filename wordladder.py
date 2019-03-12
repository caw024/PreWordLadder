#!/usr/bin/python3
import sys

def Process(infile,outfile):
  #f has lists of words to check
  f = open(infile, 'r')
  check = f.read().split('\n')
  f.close()
  
  #length of list
  i = len(check[0])
  
  #word list
  dictall = open('dictall.txt','r')
  wordlist = dictall.split('\n')
  dictall.close()
  
  mywordlist = []
  
  #get all words of same length
  for k in wordlist:
    if len(k) == i:
      mywordlist.append(k)
      
  dictionary = {}
  
  #checks per letter
  for a in check:
    k = 0
    while k < i:
      j = 97
      m = list(a)
      #change one letter of m everytime
      while j < 123:
        m[k] = chr(j)
        m = "".join(m)
        if m in mywordlist:
          if a in dictionary:
            val = dictionary[a]
            val.append(m)
            dictionary[a] = val
          else:
            dictionary[a] = m          
      
  
  #g is what we will return
  g = open(outfile,'w')
  for k in dictionary:
    g.write(k + ":" + str( len(dictionary[k])) )
  g.close()
    
            
#$ ./fred.py A.txt(words of same length) B.txt
def main():
  Process(sys.argv[1],sys.argv[2])
  
