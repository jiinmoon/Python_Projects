# Problem #27
def bubble_sort(li):
  num_passes = 0
  num_swaps = 0
  swapped = True

  while(swapped):
    swapped = False

    for i in range(0, len(li) - 1):
      if li[i] > li[i+1]:
        temp = li[i]
        li[i] = li[i+1]
        li[i+1] = temp
        num_swaps += 1
        swapped = True

    num_passes += 1
  
  return num_passes, num_swaps


def main():
  f = open('test_bubble_sort.txt', 'r')
  f.readline()
  li = list(map(lambda x: int(x), f.readline().strip().split()))
  (x,y) = bubble_sort(li)

  print('{} {}'.format(x, y))



if __name__ == '__main__':
  main()