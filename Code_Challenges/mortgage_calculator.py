# Problem #37
from math import ceil

def calc_mort(P,R,L):
  return ceil((P*(R/1200)*(1+R/1200)**L)/(((1+R/1200)**L)-1))

def main():
  f = open('test_mortgage_calculator.txt', 'r')
  (P, R, L) = map(lambda x: int(x), f.readline().strip().split())

  print(calc_mort(P,R,L))


if __name__ == '__main__':
  main()