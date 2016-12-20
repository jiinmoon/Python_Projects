# Problem #29
from collections import OrderedDict

def main():
  f = open('test_sort_with_indexes.txt', 'r')
  f.readline()

  for line in f:
    li = list(map(lambda x: int(x), line.strip().split()))
    dic = OrderedDict(sorted(zip(li, [i for i in range(1, len(li)+1)])))
    for i in dic.values():
      print(i)


if __name__ == '__main__':
  main()