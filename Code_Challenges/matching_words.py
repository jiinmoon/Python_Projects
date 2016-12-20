# Problem #55
from collections import Counter

def main():
  f = open('test_matching_words.txt', 'r')
  c = Counter(f.readline().strip().split())

  for i in sorted([x for x in c if c[x] >= 2]):
    print(i)

if __name__ == '__main__':
  main()