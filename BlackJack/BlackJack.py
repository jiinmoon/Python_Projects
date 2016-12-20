# Simple BlackJack


# created by F.Moon
# Nov.26, 2016

import math
import random

# Current Version
version = 0.1

# Playing?
playing = True

# Starting pool
pool = 100

# A Deck Defined
suits = ('C', 'S', 'D', 'H')
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

# Individual Card
class Card(object):

  def __init__(self, suit='', rank=''):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return '{}{}'.format(self.suit, self.rank)

# Playing Deck
class Deck(object):

  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit,rank))

  def __str__(self):
    deck_comp = ''
    for card in self.deck:
      deck_comp += " " + card.__str__()
    return deck_comp

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    return self.deck.pop()

# Hand for Dealer and Player
# By default, Ace = 1; If hand_value+11 busts, return to default value +1
class Hand(object):

  def __init__(self):
    self.cards = []
    self.value = 0
    self.ace = False

  def __str__(self):
    return " ".join([card.__str__() for card in self.cards])

  def add_card(self, card):
    self.cards.append(card)

    if card.rank == 'A':
      self.ace = True
    self.value += card_val[card.rank]

  def calc_val(self):
    if (self.ace == True and self.value < 12):
      return self.value + 10
    else:
      return self.value


def initialize():
  global deck, player_hand, dealer_hand, bet

  bet = 0
  deck = Deck()
  deck.shuffle()
  player_hand = Hand()
  dealer_hand = Hand()
  playing = True

def make_bet():
  global bet, pool

  print("You have ${} in bank.".format(pool))
  while True:
    try:
      user_input = int(input('Enter your bet: '))
    except TypeError:
      print('Invalid input. Try again.')
      continue
    else:
      print('Betting ${}'.format(user_input))
      if user_input >= 1 and user_input <= pool:
        bet = user_input
        break
      else:
        print('Invalid bet! You only have ${} remaining'.format(pool))
        continue

def intro():
  print("Welcome to BlackJack!\nCurrent Version: {v}\nThe goal is to reach or get closest to 21.\nGood Luck!".format(v=version))

def deal_cards():
  global deck, player_hand, dealer_hand

  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

def display_game_state():
  global player_hand, dealer_hand, bet

  print("Current Pool: ${}\tCurrent Bet: ${}".format(pool, bet))
  print("Dealer's Hand: [" + str(dealer_hand) + "]")
  print("Player's Hand: [" + str(player_hand) + "]")

def player_move():
  global player_hand, pool, bet

  user_decision = ask_player_input()

  if user_decision == 'h':
    hit()
  elif user_decision == 's':
    stand()
  elif user_decision == 'e':
    game_exit()

def hit():
  global player_hand, pool, dealer_hand, deck, bet, playing

  if playing:
    if player_hand.calc_val() <= 21:
      player_hand.add_card(deck.deal())
      
      if player_hand.calc_val() > 21:
        print("You busted!")
        pool -= bet
        playing = False

  else:
    print("Cannot hit anymore.")

  game_step()


def stand():
  global player_hand, dealer_hand, deck, bet, pool, playing

  while dealer_hand.calc_val() < 17:
    dealer_hand.add_card(deck.deal())

  if dealer_hand.calc_val() > 21:
    print("Dealer busts!")
    pool += bet
  elif dealer_hand.calc_val() < player_hand.calc_val():
    print("Your hand beat the dealer. Win!")
    pool += bet
  elif dealer_hand.calc_val == player_hand.calc_val():
    print("Tie Game...")
  else:
    print("Dealer wins...")
    pool -= bet

  playing = False
  game_step()

def ask_player_input():
  user_input = ''
  while True:
    try:
      user_input = input('Hit(h) or Stand(s) or Exit Game(e)?')
    except TypeError:
      print('Invalid input. Try again.')
      continue
    else:
      break

  return user_input

def game_step():
  global pool,playing

  print("")
  display_game_state()

  if playing == False:
    if pool == 0:
      print("Bankrupt...")
      game_exit()
    else:
      playing = True
      main()

  player_move()

def game_exit():
  print("Thanks for Playing")
  exit()

def main():
  initialize()
  make_bet()
  deal_cards()
  game_step()



if __name__ == '__main__':
  intro()
  main()
