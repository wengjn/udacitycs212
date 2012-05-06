#! /usr/bin/python
#filename: func.py

'''
this file is for the code in this lesson
to express definition of generators
'''

def sumsquare(n):
  '''not using generator in this function to get the sum of squares from 1
     to n
     too messy'''
  squares = []
  for x in range(n+1):
    squares.append(x*x)

  return sum(squares)

def sumsquares2(n):
  '''second solution to solve this problem
     use list, only one line
    uses too much memory, large list'''

  return sum([x*x for x in range(n+1)])

def sumsquares3(n):
  '''use generator here'''
  i = 0
  while i<(n+1):
    yield i*i
    i += 1

def main():
  print 'first one:', sumsquare(1000000)
  print 'second one:', sumsquares2(1000000)
  g = sumsquares3(n)
  total = 0
  for 
  print 'third one:', 

if __name__ == '__main__':
  main()
