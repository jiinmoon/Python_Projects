# Problem #94

def main():
  f = open('test_fools_day_2014.txt', 'r')

  f.readline()

  for line in f:
    print(sum(map(lambda x: int(x)**2, line.strip().split())))



if __name__ == '__main__':
  main()