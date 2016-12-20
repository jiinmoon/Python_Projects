# Problem #9
def triangle(li):
  (a,b,c) = li
  if (a + b) > c and (a + c) > b and (b + c) > a:
    return 1
  else:
    return 0

def main():
  f = open('test_triangles.txt', 'r')
  f.readline()

  for line in f:
    print(triangle(list(map(lambda x: int(x), line.strip().split()))))


if __name__ == '__main__':
  main()