# Problem #50

def main():

  f = open('test_palindrome.txt', 'r')
  f.readline()

  for line in f:
    li = list(filter(str.isalpha, line.strip().lower()))
    if li == li[::-1]:
      print('Y')
    else:
      print('N')

if __name__ == '__main__':
  main()