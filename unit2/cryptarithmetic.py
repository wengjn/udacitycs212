#! /usr/bin/python
# filename: cryptarithmetic.py

'''
solve the cryptarithmetic ODD + ODD = EVEN
'''
from __future__ import division
import itertools
import string, re

def solve(formula):
  '''Given a formula like "ODD + ODD == EVEN", fill in digits to solve it.
     Input formula is a string, output is a digit-filled-in string or None
     '''
  for f in fill_in(formula):
    if valid(f):
      return f
  
def fill_in(formula):
  '''generate all possible fillings-in of letters in formula with digits'''
  letters = ''.join(set(re.findall('[A-Z]', formula)))
  for digits in itertools.permutations('1234567890', len(letters)):
    table = string.maketrans(letters, ''.join(digits))
    yield formula.translate(table)

  

def valid(f):
  '''formula f is valid iff it has no numbers with leading zero, and evals
     true'''

  try: 
    return not re.search(r'\b0[0-9]', f) and eval(f) is True
  except ArithmeticError:
    return False


def compile_word(word):
  '''compile a word of uppercase letters as numeric digits'''

  if word.isupper():
    terms = [('%s*%s' %(10**i, d))
            for (i, d) in enumerate(word[::-1])]
    return '(' + '+'.join(terms) + ')'
  else: return word


def main():



if __name__ == '__main__':
  main()
