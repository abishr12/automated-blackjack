import random
from random import *
from random import shuffle

class Deck(object):
    
    def __init__(self):
        self.stack = [card for card in range(2,11)] * 4 + ["A", "A", "A","A"] + [10,10,10] *4
        random.shuffle(self.stack)

    def shuffle_deck(self):
        random.shuffle(self.stack)

    def produce_card(self):
        if len(self.stack) == 0:
            self.stack = [card for card in range(2,11)] * 4 + ["A", "A", "A","A"] + [10,10,10] *4
        return self.stack.pop()


class Player(object):

   def __init__(self, bankroll, name):
       self.bankroll = bankroll
       self.cards = []
       self.hand = 0
       self.name = name
       self.bet_amount = 0

   def adjust_bankroll(self, amount):
       self.bankroll += amount
       if self.bankroll <= 0:
           return "Busted"
       print("{} has ${} in the bank".format(self.name, self.bankroll))

   def bet(self):
       self.bet_amount =  randint(1, self.bankroll)
       self.bankroll -= self.bet_amount
       print("{} bets {}".format(self.name, self.bet_amount))
       return self.bet_amount

   def startRound(self,card1, card2):
       self.cards = []
       self.hand = 0
       self.cards.append(card1)
       self.cards.append(card2)
       self.calcHand()


   def calcHand(self):
       self.num_of_Aces = 0
       self.hand = 0
       for card in self.cards:
           if card == 'A':
               self.num_of_Aces += 1
           else:
               self.hand += card

       while self.num_of_Aces > 0:
           if self.hand <= 10:
               self.hand += 11
               self.num_of_Aces -=1
           else:
               self.hand += 1
               self.num_of_Aces -=1

       print("{}'s hand is -----> {}".format(self.name, self.cards))
       print("{} has a hand of {}".format(self.name, self.hand))

       return self.hand

   def pullCard(self, newCard):
       print("{} pulls card {}".format(self.name, newCard))
       self.cards.append(newCard)
       self.calcHand()


class Dealer(Player):
   def __init__(self, bankroll, name):
       self.bankroll = bankroll
       self.cards = []
       self.hand = 0
       self.name = name
       self.bet_amount = 0

   def bet(self, number):
       self.bet_amount = 0
       self.bankroll -= number
       self.bet_amount += number



adham = Player(100, "adham")
dealer = Dealer(100, "dealer")
deck = Deck()


while dealer.bankroll > 0 and adham.bankroll > 0:
   adham.bet()
   dealer.bet(adham.bet_amount)
   deck.shuffle_deck()
   dealer.startRound(deck.produce_card(), deck.produce_card())
   adham.startRound(deck.produce_card(), deck.produce_card())
   while dealer.hand < 17:
       dealer.pullCard(deck.produce_card())
   while adham.hand < 15:
       adham.pullCard(deck.produce_card())

   if dealer.hand > 21:
       print("Dealer went bust, Adham wins")
       adham.bankroll += (adham.bet_amount*2)
   elif adham.hand > 21:
       print("Adham went bust, Dealer wins")
       dealer.bankroll += (adham.bet_amount*2)
   elif adham.hand > dealer.hand:
       adham.bankroll += (adham.bet_amount*2)
       print( "Adham won round!")
   else:
       dealer.bankroll += (adham.bet_amount*2)
       print( "Dealer won this round!")

   print("Dealer's bankroll is ---->${}".format(dealer.bankroll))
   print("Adham's bankroll is ---->${}".format(adham.bankroll))

if dealer.bankroll <= 0:
    print("Adham won the game")
else:
    print("Dealer won the game")
