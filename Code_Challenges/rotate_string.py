# Problem #31


def rotate_string(shift = 0, string = ''):
  result = string[shift:] + string[0:shift]
  return result


def main():
  f = open('test_rotate_string.txt', 'r')
  f.readline()

  for line in f:
    (shift, string) = line.strip().split()
    result = rotate_string(int(shift), string)
    print(result)

if __name__ == '__main__':
  main()