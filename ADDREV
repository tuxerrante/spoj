# http://www.spoj.com/problems/ADDREV/
import re, string

#reg = re.compile("[^0]")

def zeroCleaner(s):
   if s[len(s)-1]=='0':
      # cancella zeri fino al primo non zero
      sRev = s[::-1]
      #lastZero = int( re.findall( reg, sRev)[0])
      return string.lstrip(sRev, "[^0]")
   else:
      return s[::-1]

def main():
   while True:
      N = int(raw_input())
      for i in range(N):         
         x, y = raw_input().split()
         rawSum   = int(zeroCleaner(x))+int(zeroCleaner(y))         
         #print rawSum
         print zeroCleaner(str(rawSum))
      
      return

if __name__=='__main__':
   main()
