# Problem #57

def main():
  f = open('test_smoothing_the_weather.txt', 'r')
  f.readline()

  li = list(map(lambda x: float(x), f.readline().strip().split()))
  result = []

  for i in range(0, len(li)):
    if i == 0 or i == len(li) - 1:
      result.append(li[i])
    else:
      result.append((li[i-1] + li[i] + li[i+1]) / 3.0)


  for num in result:
    print(num)

if __name__ == '__main__':
  main()