# Problem #26
def gcd(a, b):
  while not (a == b):
    if a > b:
      a -= b
    elif b > a:
      b -= a
  return a

def main():
  f = open('test_greatest_common_divisor.txt', 'r')
  f.readline()

  for line in f:
    (a, b) = map(lambda x: int(x), line.strip().split())
    gcd_ab = gcd(a,b)
    print('({} {})'.format(gcd_ab, int((a*b)/gcd_ab)))

if __name__ == '__main__':
  main()