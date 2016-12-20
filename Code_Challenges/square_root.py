# Problem #18
def herons_method(x, n):
  result = 1
  for _ in range(0, n):
    result = (result + x / result) / 2

  return result

def main():
  f = open('test_square_root.txt', 'r')
  f.readline()

  for line in f: 
    (x, n) = map(lambda x: int(x), line.strip().split())
    print(herons_method(x, n))

if __name__ == '__main__':
  main()