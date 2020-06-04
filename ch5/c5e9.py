# spbt.py backtracking parser
# Grammar:
#    <S> -> <A><B><C>
#    <A> -> 'a'
#    <A> -> ''
#    <B> -> 'b'
#    <B> -> ''
#    <C> -> 'c'
#    <C> -> ''
import sys   # needed to access command line arg

#global variables
tokenindex = -1
curchar = ''

def main():
   parser()      # call the parser

def parser():
   advance()   # prime curchar with first character
   if S():
      if curchar == '': 
         print('String in language')
      else:
         print('Garbage following string')
   else:
      print('String not in language')

def S():
   return A() and B() and C()

def A():
   if curchar == 'a':
      advance()
      return True
   elif curchar == 'b' or curchar == 'c' or curchar == '':
      return True
   else:
      return False

def B():
   if curchar == 'b':
      advance()
      return True
   elif curchar == 'c' or curchar == '':
      return True
   else:
      return False

def C():
   if curchar == 'c':
      advance()
      return True
   elif curchar == '':
      return True
   else:
      return False

def advance():
   global tokenindex, curchar
   tokenindex += 1    # move tokenindex to next token
   # check for null string or end of string
   if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
      curchar = ''    # signal the end by returning ''
   else:
      curchar = sys.argv[1][tokenindex]

def consume(expected):
   if expected == curchar:
      advance()
      return True
   else:
      return False

main()
