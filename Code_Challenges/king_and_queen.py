# Problem #53

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

def check_board(king, queen):
  if king[0] == queen[0] or king[1] == queen[1]:
    return 'Y'

  # Check Diagonal. Use slope == the slope between two positions
  # has to be 1
  (x2, y2) = queen
  if abs((y2 - king[1]) / (x2 - king[0])) == 1:
    return 'Y'

  return 'N'

def main():
  f = open('test_king_and_queen.txt', 'r')
  f.readline()

  for line in f:
    (king, queen) = line.strip().split()
    king = (dic[king[0]], int(king[1]))
    queen = (dic[queen[0]], int(queen[1]))
    print(check_board(king, queen))


if __name__ == '__main__':
  main()