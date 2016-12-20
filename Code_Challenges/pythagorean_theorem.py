# Problem #52
def test_AOR(a = 0, b = 0, c = 0):
  if (c ** 2) < a ** 2 + b ** 2:
    return 'A'
  elif (c ** 2) > a ** 2 + b ** 2:
    return 'O'
  else:
    return 'R'


def main():
  f = open('test_pythagorean_theorem.txt', 'r')

  f.readline()

  for line in f:
    (a, b, c) = map(lambda x: int(x), line.strip().split())
    print(test_AOR(a,b,c))


if __name__ == '__main__':
  main()