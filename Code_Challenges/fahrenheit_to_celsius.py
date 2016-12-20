# Problem #7
def main():
  f = open('test_fahrenheit_to_celsius.txt', 'r')
  li = map(lambda x: ((int(x) + 40)/1.8) - 40, f.read().strip().split()[1:])
  for x in li:
    print(round(x))

if __name__ == "__main__":
  main()