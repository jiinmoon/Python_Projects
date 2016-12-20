# Problem #128
from math import factorial as fact

def comb(N,K):
  return int(fact(N) / (fact(K) * fact(N - K)))

def main():
  f = open('test_combinations_counting.txt', 'r')

  f.readline()

  for line in f:
    (N, K) = map(lambda x: int(x), line.strip().split())
    print(comb(N,K))

if __name__ == '__main__':
  main()