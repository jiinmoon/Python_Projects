# Problem #59

def check_values(secret_value, guess):
  hint1 = 0
  hint2 = 0
  for (x,y) in list(zip(secret_value, guess)):
    if x == y:
      hint1 += 1
    if y in secret_value:
      hint2 += 1

  return (hint1, hint2 - hint1)

def main():
  f = open('test_bulls_and_cows.txt', 'r')

  secret_value = f.readline().strip().split()[0]

  for guess in f.readline().strip().split():
    (hint1, hint2) = check_values(secret_value, guess)
    print('{}-{}'.format(hint1, hint2))


if __name__ == '__main__':
  main()