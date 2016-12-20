# Problem #23
def checksum(li):
  result = 0
  for i in li:
    result = ((result + i) * 113) % 10000007
  return result

def main():
  f = open('test_bubble_in_array.txt', 'r')
  li = list(map(lambda x: int(x), f.readline().strip().split()[:-1]))

  num_swap = 0
  for i in range(0, len(li) - 1):
    if li[i] > li[i+1]:
      temp = li[i]
      li[i] = li[i+1]
      li[i+1] = temp
      num_swap += 1

  print('{} {}'.format(num_swap, checksum(li)))


if __name__ == '__main__':
  main()