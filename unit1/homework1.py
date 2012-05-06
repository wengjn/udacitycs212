#! /usr/bin/python
# filename: homework1.py

'''
CS212
hw1-1: 7-card stud
you have a seven card hand as input and should return the best possible 5 
card hand. The itertools library has some functions that may help.
the best hand would be ambiguous
hw1-2: Jokers (ghost card)
takes 7-card hand and return the best 5 card hand but with special card
Jokers can take any rank or suit of the same color
Black Joker: '?B', can be used as spade or club
Red Joker: '?R', can be used as heart of diamond
again the itertools library may be helpful
'''
import itertools

def best_hand(hand):
  '''from a 7-card hand, return the best 5-card hand
     could have 6*7/2=21 possibilities'''
  return max(itertools.combinations(hand, 5), key=hand_rank)

def best_wild_hand(hand):
  '''try all values for jokers in all 5-card selections.'''
  hands = set(best_hand(h)
              for h in itertools.product(*map(replacements, hand)))
  return max(hands, key=hand_rank)

def replacements(card):
  '''Return a list of the possible replacements for a card.
     There will be more than 1 only for wild cards'''
  allranks = '23456789TJQKA'
  blackcards = [r+s for r in allranks for s in 'SC']
  redcards = [r+s for r in allranks for s in 'HD']

  if card == '?B': return blackcards
  elif card == '?R': return redcards
  else: return [card]

def hand_rank(hand):
  '''Return a value indicating the ranking of a hand'''
  ranks = card_ranks(hand)  #get the numbers for every card
  if straight(ranks) and flush(hand):
    return (8, max(ranks))
  elif kind(4, ranks):
    return (7, kind(4, ranks), kind(1, ranks))
  elif kind(3, ranks) and kind(2, ranks):
    return (6, kind(3, ranks), kind(2, ranks))
  elif flush(hand):
    return (5, ranks)
  elif straight(ranks):
    return (4, max(ranks))
  elif kind(3, ranks):
    return (3, kind(3, ranks), ranks)
  elif two_pair(ranks):
    return (2, two_pair(ranks), ranks)
  elif kind(2, ranks):
    return (1, kind(2, ranks), ranks)
  else:
    return (0, ranks)

def card_ranks(hand):
  '''Return a list of the ranks(number the card), sorted with higher
     first'''
  #sample input: ['4C', '5S', '3H', 'TD']
  #sample output: [4, 5, 3, 10]
  ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
  ranks.sort(reverse=True)
  return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

def flush(hand):
  '''Return True if all the cards have the same suit'''
  #sample input: ['4C', '5C', 'JC', 'KC']
  #sample output: True
  suits = [s for r,s in hand]
  return len(set(suits)) == 1

def straight(ranks):
  '''Return True if the ordered ranks form a 5-card straight'''
  return (max(ranks)-min(ranks))==4 and len(set(ranks))==5

def kind(n, ranks):
  '''Return the first rank(bigger one) that this hand has exactly 
     n-of-a-kind of. Return None if there is no such kind in hand'''
  for r in ranks:
    if ranks.count(r) == n: return r

  return None

def two_pair(ranks):
  '''Return two ranks of two pairs if there exist such two pairs
     else return None'''
  pair = kind(2, ranks)
  lowpair = kind(2, list(reversed(ranks)))
  if pair and pair != lowpair:
    return (pair, lowpair)
  else:
    return None

def test_best_hand():
  '''test cases for the function best_hand()'''
  assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split())) 
          == ['6C', '7C', '8C', '9C', 'TC'])
  assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
          == ['8C', '8S', 'TC', 'TD', 'TH'])
  assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
          == ['7C', '7D', '7H', '7S', 'JD'])
  return 'test_best_hand passes'

def test_best_wild_hand():
  '''test cases for the function best_wild_hand()'''
  assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
          == ['7C', '8C', '9C', 'JC', 'TC'])
  assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
          == ['7C', 'TC', 'TD', 'TH', 'TS'])
  assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
          == ['7C','7D', '7H', '7S', 'JD'])
  return 'test_best_wild_hand passes'

def main():
  print test_best_hand()
  print test_best_wild_hand()

if __name__ == '__main__':
  main()
