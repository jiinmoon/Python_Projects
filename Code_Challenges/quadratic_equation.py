# Prolem #38
from numpy import sqrt

def find_roots(A,B,C):

  D = B**2 - 4*A*C

  if D < 0:
    x1 = str((-B + sqrt(D + 0j)) / (2*A))
    x2 = str((-B - sqrt(D + 0j)) / (2*A))
    if len(x1) <= 3:
      x1 = '0+' + x1[:-1] + 'i'
    else:
      x1 = x1[1:-2] + 'i'
    if len(x2) <= 3:
      x2 = '0' + x2[:-1] + 'i'
    else:
      x2 = x2[1:-2] + 'i'

  else:
    x1 = int((-B + sqrt(B**2 - 4*A*C)) / (2*A))
    x2 = int((-B - sqrt(B**2 - 4*A*C)) / (2*A))

  return str(x1), str(x2)


def main():
  f = open('test_quadratic_equation.txt', 'r')
  f.readline()

  for line in f:
    (A,B,C) = map(lambda x: int(x), line.strip().split())
    x1, x2 = find_roots(A,B,C)
    print('{} {};'.format(x1, x2))


if __name__ == '__main__':
  main()