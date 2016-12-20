# Program #43

def main():
  f = open('test_dice_rolling.txt', 'r')
  f.readline()

  for line in f:
    print(int(float(line.strip()) * 6) + 1)


if __name__ == "__main__":
  main()