def main():
  f = open('min_of_three_test.txt', 'r')
  f.readline()
  for line in f:
    print(min(map(lambda x: int(x),line.strip().split())))


if __name__ == "__main__":
  main()