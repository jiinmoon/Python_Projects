# Problem #6
def main():
  f = open('test_rounding.txt', 'r')
  f.readline()
  for line in f:
    (x,y) = line.strip().split()
    print(round(int(x)/int(y)))

if __name__ == "__main__":
  main()