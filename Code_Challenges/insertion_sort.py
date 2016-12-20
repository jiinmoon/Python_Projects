# Problem #121

def insertion_sort(li=[]):
  shift_values = []

  for i in range(1, len(li)):
    shift_value = 0
    curr = li[i]
    j = i - 1
    while j >= 0 and li[j] > curr:
      li[j+1] = li[j]
      j -= 1
      shift_value += 1
    li[j+1] = curr
    shift_values.append(str(shift_value))

  return shift_values

def main():
  f = open('test_insertion_sort.txt', 'r')
  f.readline()

  li = list(map(lambda x: int(x), f.readline().strip().split()))

  print(' '.join(insertion_sort(li)))


if __name__ == '__main__':
  main()