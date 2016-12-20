# Problem #17
def checksum(li=[]):
  result = 0

  for num in li:
    result = (((result + num) * 113) % 10000007)

  return result


def main():
  f = open('test_array_checksum.txt', 'r')
  f.readline()

  for line in f:
    print(checksum(list(map(lambda x: int(x), line.strip().split()))))



if __name__ == '__main__':
  main()