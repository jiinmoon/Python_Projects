# Problem #39
import numpy as np
from collections import OrderedDict as OD

def main():
  f = open('test_share_price_volatility.txt', 'r')
  f.readline()

  dic = OD()

  for line in f:
    li = line.strip().split()
    name = li[0]
    del li[0]
    dic[name] = list(map(lambda x: int(x), li))

  li = [k for k, v in dic.items() if np.std(v) >= 4*np.mean(v)*0.01]

  print(' '.join(li))
  

if __name__ == '__main__':
  main()