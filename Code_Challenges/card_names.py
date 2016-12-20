# Problem #58

suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def determine_card(card_value):
  global suits, ranks

  suit_value = int(card_value / 13)
  rank_value = int(card_value % 13)
  return (suits[suit_value], ranks[rank_value])



def main():
  f = open('test_card_names.txt', 'r')
  f.readline()

  li = list(map(lambda x: int(x), f.readline().strip().split()))

  for card_value in li:
    (suit, rank) = determine_card(card_value)
    print('{}-of-{}'.format(rank, suit))

if __name__ == '__main__':
  main()