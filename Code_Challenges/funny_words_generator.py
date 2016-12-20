# Problem #72

consonants = list('bcdfghjklmnprstvwxz')
vowels = list('aeiou')
X0 = 0

def linear_cong(N):
  global X0

  A = 445
  C = 700001
  M = 2097152
  li = []
  for _ in range(N):
    X0 = (A * X0 + C) % M
    li.append(X0)

  return li

def gen_fun_word(li=[]):
  result = ''

  for i in range(len(li)):
    if i % 2 == 0:
      result += consonants[li[i] % 19]
    else:
      result += vowels[li[i] % 5]

  return result

def main():
  global X0

  f = open('test_funny_words_generator.txt', 'r')

  X0 = int(f.readline().strip().split()[1])
  lis = list(map(lambda x: int(x), f.readline().strip().split()))
  for N in lis:
    print(gen_fun_word(linear_cong(N)))


if __name__ == '__main__':
  main()