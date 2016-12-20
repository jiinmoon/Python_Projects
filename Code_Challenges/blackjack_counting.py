# Problem #42

dic = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

def check_hand(hand):
  hand_value = 0
  for card in hand:
    hand_value += dic[card]

  # Ace Check
  if 'A' in hand and hand_value < 12:
    hand_value += 10

  return hand_value


def main():
  f = open('test_blackjack_counting.txt', 'r')
  f.readline()

  for line in f:
    hand_value = check_hand(line.strip().split())
    if hand_value > 21:
      print('Bust')
    else:
      print(hand_value)



if __name__ == '__main__':
  main()