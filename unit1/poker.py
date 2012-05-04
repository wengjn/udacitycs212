#! /usr/bin/python
# filename: poker.py

# want to deal the cards
import random

def card_ranks(cards):
  '''Return a list of the ranks, sorted with higher first
     ['AC', '3D', '4S', 'KH'] -> [14, 13, 4, 3]'''
  ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
  ranks.sort(reverse=True)
#return ranks
# instead of return directly, condition it
  if (ranks == [14, 5, 4, 3, 2]):
    return [5, 4, 3, 2, 1]
  else:
    return ranks

def straight(ranks):
  '''Return true if the ordered ranks from a 5-card straight.'''
  return (max(ranks)-min(ranks)==4) and len(set(ranks)) == 5
#for i in range(4):
#   if (ranks[i]-1) not in ranks:
#     return False
# return True

def flush(cards):
  '''Return true if all the cards have the same suit'''
  r = set(s for r,s in cards)
  if len(r) == 1:
    return True
  else:
    return False

def kind(n, ranks):
  '''Return the first rank that this hand has exactly n of kind.
     Return None if there is no n-of-a-kind in the hand.'''
  for r in ranks:
    if ranks.count(r) == n: return r
  return None

def two_pair(ranks):
  '''If there are two pair, return the two ranks as a tuple
     (highest, lowest); otherwise return None'''
  pair = kind(2, ranks)
  lowpair = kind(2, list(reversed(ranks)))
  if pair and lowpair != pair:
    return (pair, lowpair)
  else:
    return None

def poker(hands):
  '''Return a list of winning hands: poker([hand, ...]) -> hand
     change it to handle tie'''

  return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
  '''Return a list of all items equal to the max of the iterable'''
  result, maxval = [], None
  key = key or (lambda x: x)
  for x in iterable:
    xval = key(x)
    if not result or xval > maxval:
      result, maxval = x, xval
    elif xval == maxval:
      result.append(x)
  return result

def hand_rank(hand):
  '''get the hand rank for this hand'''
  ranks = card_ranks(hand)
  # straight flush
  if straight(ranks) and flush(hand):
    return (8, max(ranks))
  # 4 of a kind
  elif kind(4, ranks):
    return (7, kind(4, ranks), kind(1, ranks))
  # full house
  elif kind(3, ranks) and kind(2, ranks):
    return (6, kind(3, ranks), kind(2, ranks))
  # flush
  elif flush(hand):
    return (5, ranks)
  # straight
  elif straight(ranks):
    return (4, max(ranks))
  # 3 of a kind
  elif kind(3, ranks):
    return (3, kind(3, ranks), ranks)
  # 2 pairs
  elif two_pair(ranks):
    return (2, kind(2, ranks), ranks)
  # kind
  elif kind(2, ranks):
    return (1, kind(2, ranks), ranks)
  else:
  # high cards
    return (0, ranks)

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
  '''shuffle the deck and deal out numhands n-card hands.'''
  random.shuffle(deck)
  return [deck[n*i:n*(i+1)] for i in range(numhands)]

def hand_percentages(n=700*1000):
  '''sample n random hands and print a table of percentages for each type
     of hand.'''
  counts = [0] * 9
  for i in range(n/10):
    for hand in deal(5):
      ranking = hand_rank(hand)[0]
      counts[ranking] += 1
  for i in reversed(range(9)):
    print "%14s: %6.3f %%" %(hand_names[i], 100.*counts[i]/n)

def test():
  '''test cases for the functions in poker program'''
  sf = "6C 7C 8C 9C TC".split()
  fk = "9D 9H 9S 9C 7D".split()
  fh = "TD TC TH 7C 7D".split()
  tp = "5S 5D 9H 9C 6S".split()
  # only time Ace considered as 1
  al = "AC 2D 4H 3D 5S".split() # Ace-low straight, should change card_rank
  fkranks = card_ranks(fk)
  tpranks = card_ranks(tp)
  sfranks = card_ranks(sf)
  fhranks = card_ranks(fh)
  
  assert card_ranks(sf) == [10, 9, 8, 7, 6]
  assert card_ranks(fk) == [9, 9, 9, 9, 7]
  assert card_ranks(fh) == [10, 10, 10, 7, 7]
  assert straight([9, 8, 7, 6, 5]) == True
  assert straight([9, 8, 8, 6, 5]) == False
  assert flush(sf) == True
  assert flush(fk) == False
  assert kind(4, fkranks) == 9  # four of a kind
  assert kind(3, fkranks) == None  # three of a kind
  assert kind(2, fkranks) == None
  assert kind(1, fkranks) == 7   # one of kind
  assert poker([sf, fk, fh]) == sf
  assert poker([fk, fh]) == fk
  assert poker([fh, fh]) == fh
  assert poker([sf]) == sf
#assert poker([sf] + 99*[sf]) == sf
  assert hand_rank(sf) == (8, 10)
  assert hand_rank(fk) == (7, 9, 7)
#  assert hand_rank(fh) == (6, 10, 7)
  return "tests pass"


def main():
  print test()
  print deal(2)

if __name__ == '__main__':
  main()
