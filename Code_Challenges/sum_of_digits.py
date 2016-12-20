# Problem #11

def sumOfDigits(li=[]):
  sums = 0
  x = 0
  value = li[0] * li[1] + li[2]
  
  while value > 0:
    x = value % 10
    sums += x
    value = int(value/10)

  print(sums)

def main():
  f = open('test_sum_of_digits.txt', 'r')
  f.readline()


  for line in f:
    li = list(map(lambda x: int(x), line.strip().split()))
    sumOfDigits(li)


if __name__ == "__main__":
  main()