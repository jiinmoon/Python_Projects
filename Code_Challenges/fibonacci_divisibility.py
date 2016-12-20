# Problem #69

dic = {0: 0, 1: 2, 2: 3, 3: 4, 5: 5, 8: 6}
prev = 5
curr = 8
curr_index = 6

def find_fib(num):
  global dic

  for x, y in sorted(dic.items()):
    if not x == 0 and x % num == 0:
      return y
  
  return find_more_fibs(num)

def find_more_fibs(num):
  global dic, curr, prev, curr_index

  while(not (curr % num == 0)):
    prev, curr = curr, curr + prev
    dic[prev] = curr_index
    curr_index += 1

  return curr_index

def main():
  f = open('test_fibonacci_divisibility.txt', 'r')
  f.readline()

  for num in list(map(lambda x: int(x), f.readline().strip().split())):
    print(find_fib(num))


if __name__ == '__main__':
  main()