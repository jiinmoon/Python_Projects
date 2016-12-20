# Problem #120
def selection_sort(li=[]):
  max_indexes = []

  for i in range(len(li)-1, 0, -1):
    max = 0
    for j in range(0, i+1):
      if li[j] > li[max]:
        max = j

    temp = li[i]
    li[i] = li[max]
    li[max] = temp
    max_indexes.append(str(max))

  return max_indexes

def main():
  f = open('test_selection_sort.txt', 'r')
  f.readline()

  li = list(map(lambda x: int(x), f.readline().strip().split()))

  print(' '.join(selection_sort(li)))

if __name__ == '__main__':
  main()