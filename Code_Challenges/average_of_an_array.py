# Problem #16
def rounding(num):
  r_num = round(num)
  if num - r_num >= 0.5:
    return r_num + 1
  else:
    return r_num


def main():
  f = open('test_average_of_an_array.txt', 'r')
  f.readline()

  for line in f:
    li = list(map(lambda x: int(x), line.strip().split()[:-1]))
    print(rounding(sum(li)/len(li)))


if __name__ == '__main__':
  main()