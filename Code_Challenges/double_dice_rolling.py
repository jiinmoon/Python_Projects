# Problem #44

def main():
  f = open('test_double_dice_roll.txt', 'r')
  f.readline()
  for line in f:
    (x, y) = map(lambda x: int(x), line.strip().split())
    print((x%6 + 1) + (y%6 +1))

if __name__ == '__main__':
  main()