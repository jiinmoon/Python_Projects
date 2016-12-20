# Problem #61
primes = []

def primes_sieve(max_index):
  global primes

  limitn = 20000000+1
  not_prime = [False] * limitn

  for i in range(2, limitn):
    if not_prime[i]:
          continue
    for f in range(i*i, limitn, i):
      not_prime[f] = True

    primes.append(i)

    if len(primes) > max_index:
      break

  return primes


def main():
  global primes

  f = open('test_prime_numbers_generator.txt', 'r')
  f.readline()

  li = list(map(lambda x: int(x), f.readline().strip().split()))
  max_index = max(list(li))

  primes_sieve(max_index)
  for i in li:
    print(primes[i-1])


if __name__ == '__main__':
  main()