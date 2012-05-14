#! /usr/bin/python
# filename: zebra.py

'''
1 There are five houses.
2 The Englishman lives in the red house.
3 The Spaniard owns the dog.
4 Coffee is drunk in the green house.
5 The Ukrainian drinks tea.
6 The green house is immediately to the right of the ivory house.
7 The Old Gold smoker owns snails.
8 Kools are smoked in the yellow house.
9 Milk is drunk in the middle house.
10 The Norwegian lives in the first house.
11 The man who smokes Chesterfields lives in the house next to the man with the fox.
12 Kools are smoked in a house next to the house where the horse is kept.
13 The Lucky Strike smoker drinks orange juice.
14 The Japanese smokes Parliaments.
15 The Norwegian lives next to the blue house.
Who drinks water? Who owns the zebra?
Each house is painted a different color, and their inhabitants are of different nationalities, own different pets, drink different beverages and smoke different brands of American cigarettes.
'''
import itertools
import time

def timedcall(fn, *args):
  '''call function with args; return the time in seconds and result'''
  t0 = time.clock()
  result = fn(*args)
  t1 = time.clock()
  return t1-t0, result

def timedcalls(n, fn, *args):
  '''call fn(*args) repeatedly: n times if n is an int, or up to 
     n seconds if n is a float; return the min, average, and max time'''
  # if n is integer
  if isinstance(n, int):
      times = [timedcall(fn, *args)[0] for i in range(n)]
  else:
    times = []
    while sum(times)<n:
      times.append(timedcall(fn, *args)[0])
  return min(times), average(times), max(times)

def ints(start, end = None):
  '''generator, from start to end, if end not specified, to infinite'''
  i = start
  while i <= end or end is None:
    yield i
    i += 1

def all_ints():
  '''generate integers in the order 0, +1, -1, +2, -2, +3, -3,...'''
  yield 0
  i = 1
  while True:
    yield +i
    yield -i
    i += 1


def average(numbers):
  '''Return the average (arithmetic mean) of a sequence of numbers'''
  return sum(numbers)/float(len(numbers))

def c(sequence):
  '''generate items in sequence; keeping counts as we go, c.starts is the
  number of sequence started; c.items is the number of items generated'''
  c.start += 1
  for item in sequence:
    c.items += 1
    yield item

def nextto(h1, h2):
  '''two house are next to each other if they differ by 1'''
  return abs(h1-h2) == 1

def imright(h1, h2):
  '''house h1 is immediately right of h2 if h1-h2==1'''
  return h1-h2 == 1

def zebra_puzzle():
  '''solve the zebra puzzle, return a tuple(water, zebra)'''
  houses = [first,_,middle,_,_] = [1,2,3,4,5]
  orderings = list(itertools.permutations(houses))
  return next((WATER, ZEBRA)
          for(red, green, ivory, yellow, blue) in orderings
          if imright(green, ivory)
          for(Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
          if Englishman is red
          if Norwegian is first
          if nextto(Norwegian, blue)
          for(coffee, tea, milk, oj, WATER) in orderings
          if coffee is green
          if Ukranian is tea
          if milk is middle
          for(OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
          if Kools is yellow
          if LuckyStrike is oj
          if Japanese is Parliaments
          for(dog, snails, fox, horse, ZEBRA) in orderings
          if Spaniard is dog
          if OldGold is snails
          if nextto(Chesterfields, fox)
          if nextto(Kools, horse)
          )

def c(sequence):
  '''keep count and item of the sequence'''
  c.starts += 1
  for item in sequence:
    c.item += 1
    yield item

def instrument_fn(fn, *args):
  c.starts, c.items = 0, 0
  result = fn(*args)
  print ('%s got %s with %5d iters over %7d items' %(
              fn.__name__, result, c.starts, c.items))


def main():
  print zebra_puzzle()

if __name__ == '__main__':
  main()

