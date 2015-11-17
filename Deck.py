#Rodrigo
#COM 110
#Assignment 5
#Due: November 8, 2013 9:30 p.m.

from random import*
from PlayingCard import PlayingCard
from graphics import *

class Deck: 
    
    def __init__(self):      
        self.deck = []
        xpos = 725
        ypos = 150
        offset = 0
        for suit in ["d","c","h","s"]:
            for rank in range(1,14):               
                self.deck.append(PlayingCard(rank,suit))
    
    def shuffle(self): 
        for j in range(len(self.deck)):
            c = self.deck[j]
            i = randrange(52)
            card = self.deck[i]
            self.deck[i] = c
            self.deck[j] = card
        return self.deck 
            
    def dealCard(self):
        dealtCard= self.deck.pop(0)  
        return dealtCard
               
    def cardsLeft(self): 
        length = len(self.deck)
        return length
              
if __name__=="__main__": 
    main()   
