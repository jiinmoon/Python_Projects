# Problem #32
def josephus(n, k):
  if n == 1:
    return 1
  else:
    return (josephus(n-1, k) + k - 1) % n + 1;

def main():
  f = open('test_josephus_problem.txt', 'r')
  (n, k) = f.readline().strip().split()
  print(josephus(int(n), int(k)))


if __name__ == '__main__':
  main()