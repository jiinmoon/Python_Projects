# Problem #67

dic = {0: 0, 1: 2, 2: 3, 3: 4, 5: 5, 8: 6}
prev = 5
curr = 8
curr_index = 6

def find_fib(num):
  global dic, curr, prev, curr_index

  while(not (num in dic)):
    prev, curr = curr, curr + prev
    dic[prev] = curr_index
    curr_index += 1

  return dic[num]

def main():
  f = open('test_fibonacci_sequence.txt', 'r')
  f.readline()

  for line in f:
    print(find_fib(int(line.strip())))


if __name__ == '__main__':
  main()