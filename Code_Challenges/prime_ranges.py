# Problem #61
primes = {}

def primes_sieve():
  global primes

  limitn = 3000000
  not_prime = [False] * limitn
  index = 0

  for i in range(2, limitn):
    if not_prime[i]:
          continue
    for f in range(i*i, limitn, i):
      not_prime[f] = True

    primes[i] = index
    index += 1

  return primes


def main():
  global primes

  f = open('test_prime_ranges.txt', 'r')
  f.readline()

  primes_sieve()

  for line in f:
    x, y = line.strip().split()
    print(primes[int(y)] - primes[int(x)] + 1)


if __name__ == '__main__':
  main()