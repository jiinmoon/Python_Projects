# Problem #35

def calc_saving(S, R, P):
  years = 0
  while(S < R):
    S += (S * (P/100))
    years += 1

  return years

def main():
  f = open('test_savings_calculator.txt', 'r')
  f.readline()
  for line in f:
    (S, R, P) = map(lambda x: float(x), line.strip().split())
    print(calc_saving(S,R,P))

if __name__ == '__main__':
  main()