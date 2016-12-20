# Problem #81

from collections import Counter

# return 32bit, string representation of binary num
def to_bin(num):
  result = ''
  for _ in range(32):
    result += str(int(num % 2))
    num /= 2
  return result[::-1]

def main():
  f = open('test_bit_count.txt', 'r')
  f.readline()
  li = list(map(lambda x: int(x), f.readline().strip().split()))
  for num in li:
    print(Counter(list(to_bin(num)))['1'])


if __name__ == '__main__':
  main()