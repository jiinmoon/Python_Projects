# Problem #10
def lin_function(x1,y1,x2,y2):
  a = (y2 - y1) / (x2 - x1)
  b = y1 - a * x1
  return int(a), int(b)


def main():
  f = open('test_linear_function.txt', 'r')
  f.readline()

  for line in f:
    (x1, y1, x2, y2) = map(lambda x: int(x),line.strip().split())
    (a,b) = lin_function(x1,y1,x2,y2)
    print('({} {})'.format(a, b))

if __name__ == '__main__':
  main()