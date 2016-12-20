# Problem #68

def main():
  f = open('test_bicycle_race.txt', 'r')

  f.readline()
  for line in f:
    (S, A, B) = map(lambda x: float(x), line.strip().split())
    print(A*(S/(A+B)))


if __name__ == '__main__':
  main()