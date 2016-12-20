# Problem #30

def main():
  f = open('test_reverse_string.txt', 'r')

  i = list(f.read().strip())
  i.reverse()
  print(''.join(i))

if __name__ == '__main__':
  main()