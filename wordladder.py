#!/usr/bin/python3
import sys

def Process(infile,outfile):
  #f has lists of words to check
  f = open(infile, 'r')
  check = f.read().split('\n')
  f.close()

  p = 0
  while p < len(check):
    check[p] = ''.join(check[p].split())
    p+=1
  
  #length of list
  length = len(check[0])
  print(length)
  
  #word list
  dictall = open('dictall.txt','r')
  wordlist = dictall.read().split('\n')
  dictall.close()
  
  mywordlist = []
  
  #get all words of same length
  for k in wordlist:
    if len(k) == length:
      mywordlist.append(k)
  #print(k)
      
  dictionary = {}
  
  #checks per letter
  for word in check:
    print("new word: " + word)
    index = 0
    if len(word) == length:
      dictionary[word] = []
    else:
      index = length
    while index < length:
      j = 97
      #change one letter of m everytime
      print(index)
      while j < 123:
        m = list(word)
        m[index] = chr(j)
        m = "".join(m)
        #print(m in mywordlist)
        if m in mywordlist:
          if m == word:
            pass
          else:
            val = dictionary[word]
            val.append(m)
            dictionary[word] = val
        j+=1
      index+=1
      
  
  #g is what we will return
  g = open(outfile,'w')
  for k in check:
    if k in dictionary:
      g.write(k + "," + str( len(dictionary[k])) + "\n" )
  g.close()

            
#$ ./fred.py A.txt(words of same length) B.txt
def main():
  Process(sys.argv[1],sys.argv[2])

main()
