# Problem #21

from collections import Counter

def main():
  f = open('test_array_counters.txt', 'r')
  f.readline()

  for line in f:
    for num in dict(Counter(map(lambda x: int(x), line.strip().split()))).values():
      print(num)


if __name__ == '__main__':
  main()