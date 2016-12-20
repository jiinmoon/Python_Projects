# Tie-Tac-Toe

# Francisco Moon
# Nov.25, 2016


from IPython.display import clear_output
from random import randint
import string

# display_current board state
def display_board(board):
  clear_output()
  print('{} | {} | {}'.format(board[7], board[8], board[9]))
  print('- + - + -')
  print('{} | {} | {}'.format(board[4], board[5], board[6]))
  print('- + - + -')
  print('{} | {} | {}'.format(board[1], board[2], board[3]))

# take in player input. Player is 'O'
def player_move(board):
  while True:
    user_input = int(input('Enter your move: '))

    #Valid Input Check
    if user_input in range(1,10) and not (board[user_input] == 'X' or board[user_input] == 'O'):
      board[user_input] = 'O'
      break
    else:
      print('Incorrect move. Try again.')

def ai_move(board):
  while True:
    # randomly assign 'X' to board spot if available
    ai_move_position = randint(1,9)

    if not (board[ai_move_position] == 'X' or board[ai_move_position] == 'O'):
      board[ai_move_position] = 'X'
      break

def win_check(board):
  # player wins returns 1. ai wins returns -1. 
  # tie returns 2. else 0.
  
  if ('O' == board[1] and 'O' == board[2] and 'O' == board[3]) or ('O' == board[4] and 'O' == board[5] and 'O' == board[6]) or ('O' == board[7] and 'O' == board[8] and 'O' == board[9]) or ('O' == board[7] and 'O' == board[4] and 'O' == board[1]) or ('O' == board[8] and 'O' == board[5] and 'O' == board[2]) or ('O' == board[9] and 'O' == board[6] and 'O' == board[3]) or ('O' == board[7] and 'O' == board[5] and 'O' == board[3]) or ('O' == board[9] and 'O' == board[5] and 'O' == board[1]):
    # Player 1 wins
    return 1
  elif ('X' == board[1] and 'X' == board[2] and 'X' == board[3]) or ('X' == board[4] and 'X' == board[5] and 'X' == board[6]) or ('X' == board[7] and 'X' == board[8] and 'X' == board[9]) or ('X' == board[7] and 'X' == board[4] and 'X' == board[1]) or ('X' == board[8] and 'X' == board[5] and 'X' == board[2]) or ('X' == board[9] and 'X' == board[6] and 'X' == board[3]) or ('X' == board[7] and 'X' == board[5] and 'X' == board[3]) or ('X' == board[9] and 'X' == board[5] and 'X' == board[1]):
    # AI wins
    return -1
  elif (len(set(board)) == 3):
    return 2
  else:
    return 0

def initialize():
  board = [i for i in range(0,10)]
  return board

def main():
  board = initialize()
  print("<> <> <> Tie-Tac-Toe <> <> <>")
  print("Tie to win!")

  display_board(board)

  win = 0
  while win == 0:
    player_move(board)

    win = win_check(board)
    if (win == 1):
      print("AI Wins...")
      break
    elif (win == -1):
      print("AI Wins...")
      break
    elif (win == 2):
      print("It's a tie. You WIN!")
      break
    ai_move(board)
    display_board(board)

  user_input = str(input('Play again? Y/N'))
  if user_input.lower() == 'y':
    main()
  else:
    print("Good Bye.")

if __name__ == '__main__':
  main()
