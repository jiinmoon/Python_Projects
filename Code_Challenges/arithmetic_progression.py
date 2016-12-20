# Problem #8
def arithp(li):
  A = li[0]
  B = li[1]
  i = li[2]
  value = 0
  for x in range(0, i):
    value += A + (x * B)
  print(value)


def main():
  f = open('test_arithmetic_progression.txt', 'r')
  f.readline()

  for line in f:
    arithp(list(map(lambda x: int(x), line.strip().split())))


if __name__ == '__main__':
  main()