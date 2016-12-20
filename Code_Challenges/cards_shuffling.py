# Problem #45

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']


def main():
  deck = []

  for suit in suits:
    for rank in ranks:
      deck.append(suit+rank)

  f = open('test_cards_shuffling.txt', 'r')
  li = list(map(lambda x: int(x) % 52, f.readline().strip().split()))
  li.reverse()

  for i in range(0, 52):
    j = li.pop()
    tmp = deck[j]
    deck[j] = deck[i]
    deck[i] = tmp

  print(' '.join(deck))

if __name__ == '__main__':
  main()