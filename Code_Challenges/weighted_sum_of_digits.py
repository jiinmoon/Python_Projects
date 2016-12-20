# Problem #13
def wsd(num):
  x = list(map(lambda x: int(x), list(num)))
  y = [i for i in range(1, len(x) + 1)]
  print(sum([x*y for x,y in zip(x,y)]))


def main():
  f = open('test_weighted_sum_of_digits.txt', 'r')
  f.readline()

  for num in f.read().split():
    wsd(num)

if __name__ == "__main__":
  main()