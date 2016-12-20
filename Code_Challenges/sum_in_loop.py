import sys

def sum_in_loop(l=[]):
  sum = 0
  for i in l:
    sum += i
  return sum

def main():
  f = open('test.txt', 'r')
  print(sum_in_loop(map(lambda x: int(x), f.read().split()[1:])))

if __name__ == "__main__":
  main()