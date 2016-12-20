# Problem #48
def collatz(num = 0):
  count = 0

  while (not num == 1):
    if num % 2 == 0:
      num /= 2
    else:
      num = 3 * num + 1
    count += 1

  return count

def main():
  f = open('test_collatz_sequence.txt', 'r')
  f.readline()

  for num in map(lambda x: int(x), f.readline().strip().split()):
    print(collatz(num))



if __name__ == '__main__':
  main()