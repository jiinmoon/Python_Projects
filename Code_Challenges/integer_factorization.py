# Problem #63
primes = []

def prime(n):
  global primes

  if n <= 2:
    primes = []
  sieve = [True] * (n+1)
  for x in range(3, int(n**0.5) + 1, 2):
    for y in range(3, (n//x) + 1, 2):
      sieve[(x*y)] = False

  primes = [2] + [i for i in range(3, n, 2) if sieve[i]]

def prime_fact(n):
  global primes

  result = ''
  for prime in primes:
    while (True):
      if n % prime == 0:
        n //= prime
        result += str(prime) + '*'
      else:
        break
  return result[:-1]


def main():
  f = open('test_integer_factorization.txt', 'r')
  f.readline()

  data = [int(i.strip()) for i in f.read().split()]
  prime(int(max(data)**(.5)))

  for n in data:
    print(prime_fact(n))

if __name__ == '__main__':
  main()