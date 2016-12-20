# Problem #24
def pseudorandom(num):
  num *= num
  num = str(num)
  while(not len(num) == 8):
    num = '0' + num  
  return int(num[2:6])


def check_loop(num):
  num_iter = 0
  li = [num]
  while(True):
    num = pseudorandom(num)
    num_iter += 1
    if num in li:
      return num_iter
    else:
      li.append(num)



def main():
  f = open('test_neumanns_random_generator.txt', 'r')
  f.readline()
  for num in map(lambda x: int(x), f.readline().strip().split()):
    print(check_loop(num))

if __name__ == '__main__':
  main()