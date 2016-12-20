# Problem #46
def check_win_condition(X,O):

  if 1 in X and 2 in X and 3 in X or 1 in O and 2 in O and 3 in O:
    return True
  elif 4 in X and 5 in X and 6 in X or 4 in O and 5 in O and 6 in O:
    return True
  elif 7 in X and 8 in X and 9 in X or 7 in O and 8 in O and 9 in O:
    return True
  elif 1 in X and 5 in X and 9 in X or 1 in O and 5 in O and 9 in O:
    return True
  elif 3 in X and 5 in X and 7 in X or 3 in O and 5 in O and 7 in O:
    return True
  elif 1 in X and 4 in X and 7 in X or 1 in O and 4 in O and 7 in O:
    return True
  elif 2 in X and 5 in X and 8 in X or 2 in O and 5 in O and 8 in O:
    return True
  elif 3 in X and 6 in X and 9 in X or 3 in O and 6 in O and 9 in O:
    return True
  else:
    return False


def check_win_moves(moves):

  num_moves = 0
  X = []
  O = []

  for i in range(9):
    if i % 2 == 0:
      X.append(moves[i])
    else:
      O.append(moves[i])
    num_moves +=1

    if len(X) >= 3:
      if check_win_condition(X,O):
        return num_moves

  return 0



def main():
  f = open('test_tic_tac_toe.txt', 'r')

  f.readline()

  for line in f:
    moves = list(map(lambda x: int(x), line.strip().split()))
    print(check_win_moves(moves))

if __name__ == '__main__':
  main()