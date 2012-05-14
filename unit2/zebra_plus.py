#! /usr/bin/python
# filename: zebra_plus.py

'''
with additional output
this output is smart one
'''

def find_water_zebra():
  import itertools

  houses = [first, _, middle, _, _] = [1,2,3,4,5]
  orderings = list(itertools.permutations(houses))

  def imright(h1, h2):
    return h1-h2 == 1

  def nextto(h1, h2):
    return abs(h1-h2)==1

  return [result for result in (
          (
            ('Drinks', {'coffee':coffee, 'tea':tea, 'milk':milk, 'WATER':WATER, 'oj':oj}),
            ('Nations', {'Englishman':Englishman, 'Spaniard':Spaniard, 'Ukranian':Ukranian, 'Japanese':Japanese, 'Norwegian':Norwegian}),
            ('Colours',{'red':red, 'green':green, 'ivory':ivory, 'yellow':yellow, 'blue':blue}),
            ('Pets', {'dog':dog, 'snails':snails, 'fox':fox, 'horse':horse, 'ZEBRA':ZEBRA}),
            ('Smokes', {'OldGold':OldGold, 'Kools':Kools, 'Chesterfields':Chesterfields, 'LuckyStrike':LuckyStrike, 'Parliaments':Parliaments}),
          )

          for (red, green, ivory, yellow, blue) in orderings
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
          if nextto(Kools, horse)
          if nextto(Chesterfields, fox)
          )
       ]

def main():
  hps = find_water_zebra()
  print 'Result count:', len(hps)
  if len(hps) < 20:
    for hp in hps:
      print 'House ', ''.join('%15s'%(num if num else 'House') for num in range(1, 6))
      for item, props in hp:
        propKeys = sorted(props.keys(), key=lambda k: props[k])
        print '%-7s'%item, ''.join(['%15s'%propKey for propKey in propKeys])

if __name__ == '__main__':
  main()
