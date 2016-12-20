def main():
  f = open('test_sums_in_loop.txt', 'r')
  f.readline()
  for line in f:
    (x,y) = line.strip().split()
    print(int(x)+int(y))

if __name__ == "__main__":
    main()