# Problem #22
from math import ceil


def two_printer(x,y,n):
  T = ceil( n / (1/x + 1/y) )
  while(True):
    if T % x == 0 or T % y == 0:
      return T
    else:
      T += 1


def main():
  f = open('test_two_printers.txt', 'r')
  f.readline()

  for line in f:
    (x,y,n) = list(map(lambda x: int(x), line.strip().split()))
    print(two_printer(x,y,n))

if __name__ == '__main__':
  main()