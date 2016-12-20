# Problem #34

from math import sqrt, exp

def bin_search(A, B, C, D, lo, hi):
  X = (lo + hi) / 2
  result = (A * X) + (B * sqrt(X ** 3)) - (C * exp( (-X) / 50)) - D

  if -0.0000001 < result < 0.0000001:
    return X

  if result > 0:
    return bin_search(A,B,C,D,lo,X)
  else:
    return bin_search(A,B,C,D,X,hi)

def main():
  f = open('test_binary_search.txt', 'r')

  f.readline()

  for line in f:
    (A,B,C,D) = list(map(lambda x: float(x), line.strip().split()))
    X = bin_search(A, B, C, D, 0, 100)
    print(X)


if __name__ == '__main__':
  main()