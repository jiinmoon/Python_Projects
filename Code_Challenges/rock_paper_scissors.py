# Problem #49

dic = {'RR': 0, 'PP': 0, 'SS': 0, 'RP': -1, 'PR': 1, 'SR': -1, 'RS': 1, 'PS': -1, 'SP': +1}

def rps_winner(records):
  winner = 0
  for game in records:
    winner += dic[game]

  if winner > 0:
    return 1 
  else:
    return 2

def main():
  f = open('test_rock_paper_scissors.txt', 'r')
  f.readline()
  for line in f:
    print(rps_winner(line.strip().split()))


if __name__ == '__main__':
  main()