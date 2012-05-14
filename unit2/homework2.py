#! /usr/bin/python
# filename: homework2.py

import re
import itertools
import string

def compile_formula(formula, verbose=False):
  '''compile formula into a function. also return letters found, as a str
     in same order as parms of function. The first digit of a multi-digit
     number cannot be 0. So if YOU is a word in the formula, and the func
     is called with Y equal to 0, the func should return False'''

  letters = ''.join(set(re.findall('[A-Z]', formula)))
  parms = ', '.join(letters)
  tokens = map(compile_word, re.split('([A-Z]+)', formula))
  body = ''.join(token
