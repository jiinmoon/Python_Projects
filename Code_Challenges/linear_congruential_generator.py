# Problem #25

def find_n(A, C, M, X0, N):
  for _ in range(N):
    X0 = (A * X0 + C) % M
  return X0


def main():
  f = open('test_linear_congruential_generator.txt', 'r')
  f.readline()

  for line in f:
    (A, C, M, X0, N) = map(lambda x: int(x), line.strip().split())
    print(find_n(A,C,M,X0,N))

if __name__ == '__main__':
  main()