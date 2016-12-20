def main():
  f = open('test_maximum_of_array.txt','r')
  l = list(map(lambda x: int(x.strip()), f.read().split()))

  print(max(l), min(l))

if __name__ == "__main__":
  main()