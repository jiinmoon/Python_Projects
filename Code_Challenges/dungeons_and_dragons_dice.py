# Problem #51
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

dices = [1,2,3,4,5]
sides = [2,4,6,8,10,12]
dic = {}

def generate_dice_table():
  global dices, sides, dic

  for side in sides:
    for dice in dices:
      li = []
      for _ in range(1000):
        sum1 = 0
        for _ in range(dice):
          sum1 += np.random.randint(1,side+1)
        
        li.append(sum1)

      dic['{}d{}'.format(dice, side)] = li

def main():
  generate_dice_table()

  f = open('test_dungeons_and_dragons_dice.txt', 'r')


  for line in f:
    li = list(map(lambda x: int(x), line.strip().split()[:-1]))
    mean_li = sum(li)/len(li)
    max_li = max(li)
    min_li = min(li)

    for x, y in dic.items():
      mean_x = sum(dic[x])/len(dic[x])
      if mean_li - .5 < mean_x < mean_li + .5:
        (dice, side) = x.split('d')
        if (int(dice) * int(side)) >= max_li and int(x[0]) <= min_li:
          print(x, mean_x, mean_li)
    print('-')

if __name__ == '__main__':
  main()