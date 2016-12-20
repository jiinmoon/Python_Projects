# Problem #104
from math import sqrt

def dist(X1, Y1, X2, Y2, X3, Y3):
  a = sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
  b = sqrt((X3 - X1)**2 + (Y3 - Y1)**2)
  c = sqrt((X3 - X2)**2 + (Y3 - Y2)**2)
  return (a, b, c)

def heron(a, b, c):
  S = (a + b + c) / 2
  return sqrt(S*(S-a)*(S-b)*(S-c))

def main():
  f = open('test_triangle_area.txt', 'r')
  f.readline()

  for line in f:
    (X1, Y1, X2, Y2, X3, Y3) = map(lambda x: int(x), line.strip().split())
    (a, b, c) = dist(X1, Y1, X2, Y2, X3, Y3)
    print(heron(a, b, c))

if __name__ == '__main__':
  main()