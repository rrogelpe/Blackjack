#Rodrigo Rogel-Perez
#COM 110
#Assignment 5
#Due: November 8, 2013 9:30 p.m.

class PlayingCard:

    def __init__(self, rank, suit): 
        self.rank = rank 
        self.suit = suit 
        self.ranks = {1:"Ace",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"Jack",12:"Queen",13:"King"}
        self.suits = {"s":"Spades","d":"Diamonds","h":"Hearts","c":"Clubs"}

    def getRank(self): #method which returns the rank of the card
        return self.rank

    def getSuit(self):#method which returns the suit of the card
        return self.suit
        
    def BJValue(self):       
        #hasAce = False
        if self.rank >= 11:
            self.rank = 10
        #if self.rank == 1:
            #hasAce = True
        #else:
            #hasAce = False
        return self.rank
            
    def __str__(self):      
        return(self.ranks[self.rank] + " of " + self.suits[self.suit])
       
if __name__=="__main__": 
    main()
        

        
