# c4e1 parser
# Grammar:
#    <S> -> 'a'<S>'b'
#    <S> -> 'c'
import sys   # needed to access command line arg

#global variables
tokenindex = -1
lenabu = 0
token = ''

def main():
   try:
      parser()      # call the parser
   except RuntimeError as emsg:
      print(emsg)

def advance():
   global tokenindex, token
   tokenindex += 1    # move tokenindex to next token
   # check for null string or end of string
   if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
      token = ''      # signal the end by returning ''
   else:
      token = sys.argv[1][tokenindex]

def consume(expected):
   if expected == token:
      advance()
   else:
      raise RuntimeError('Expecting ' + expected)

def parser():
   advance()   # prime token with first character
   S()         # call function for start symbol
   # test if end of input string
   if token != '': 
      print('Garbage following <S>-string')
   
def S():
    global lenabu
    consume('a')
    while token == 'a':
        advance()
        lenabu += 1
    consume('c')
    while token == 'b' and lenabu != 0:
        advance()
        lenabu -= 1
    consume('b')


main()
