def main():
  f = open('test_minimum_of_two.txt','r')
  f.readline()
  for line in f:
    (x,y) = line.strip().split()
    if int(x) < int(y):
      print(x)
    else:
      print(y)

if __name__ == "__main__":
  main()