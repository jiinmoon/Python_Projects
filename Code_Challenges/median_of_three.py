# Problem #41
def median_of_three(li):
  (x,y,z) = li
  if x < y < z or z < y < x:
    return y
  elif y < x < z or z < x < y:
    return x
  else:
    return z

def main():
  f = open('test_median_of_three.txt', 'r')

  f.readline()
  for line in f:
    li = list(map(lambda x: int(x), line.strip().split()))
    #print(li)
    print(median_of_three(li))




if __name__ == "__main__":
  main()