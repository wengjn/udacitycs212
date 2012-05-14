#! /usr/bin/python
# filename: homework2_floor.py

'''
floor puzzle

Hopper, Kay, Liskov, Perlis and Ritchie live on different floors of a 
5-floor apartment building.

Hopper doesn't live on the top floor
Kay does not live on the bottom floor
Liskov does not live on either the top or the bottom floor
Perlis lives on a higher floor than Kay does.
Ritchie does not live on a floor adjacent to Liskov's
Liskov does not live on a floor adjacent to Kay's

where does everyone live?
floor_puzzle() returns a list of five floor numbers denoting everyone
'''

import itertools

def floor_puzzle():
  '''returns a list of 5-floor numbers denoting the floor of everyone'''
  floors = [bottom, _,_,_,top] = [1,2,3,4,5]
  orderings = list(itertools.permutations(floors))
  
  for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
    if (Hopper is not top
        and Kay is not bottom
        and Liskov is not top 
        and Liskov is not bottom
        and Perlis > Kay
        and abs(Ritchie - Liskov) > 1
        and abs(Liskov - Kay) > 1):
      return [Hopper, Kay, Liskov, Perlis, Ritchie]

def main():
  print floor_puzzle()

if __name__ == '__main__':
  main()
