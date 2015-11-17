#Rodrigo Rogel-Perez
#Virginia Gresham
#COM 110
#Assignment 5
#Due: November 8, 2013 9:30 p.m.

from random import*
from Deck import *
from Button import *
from graphics import *

class BlackJack: #class defined with name
    
    def __init__(self):#object constructor for the class with definition
        #normal parameters follow the self parameter(the object to which the instance variables are applied)
        #initializes the instance variables
        """constructor that initializes instance variables
        it also gives the playingDeck an initial shuffle"""
        self.dHand = [] #instance variable where data is stored
        self.pHand = [] #instance variable where data is stored
        self.images = []
        self.bank = 50
    def getdHand(self):
        return self.dHand    
    def getpHand(self):
        return self.pHand
    def getBank(self):
        return self.bank
    def initDeal(self, gwin, xposD, yposD, xposP, yposP):
        """deals out initial cards, two per player, and displays dealer
        and player hands on graphical win xposD and yposD give initial
        position for dealer cards xposP and yposP are analogous"""
        #the normal parameters xposD, yposD, xposP, yposP give you
        #the initial positions of the cards that the dealer/player is dealt
        #the gwin parameter draws these initial cards to the GUI created
        #draw cards to these points

        self.deck = Deck()
        self.deck.shuffle()
        
        xcardD = self.deck.dealCard()
        self.dHand.append(xcardD)
        xcardDealerImage = Image(xposD,"playingcards/"+ xcardD.suit + str(xcardD.rank) +".gif")
        xcardDealerImage.draw(gwin)
        self.images.append(xcardDealerImage)
        
        ycardD = self.deck.dealCard()
        self.dHand.append(ycardD)
        ycardDealerImage = Image(yposD,"playingcards/"+ ycardD.suit + str(ycardD.rank) +".gif")
        ycardDealerImage.draw(gwin)
        self.images.append(ycardDealerImage)
        
        xcardP = self.deck.dealCard()
        self.pHand.append(xcardP)
        xcardPlayerImage = Image(xposP,"playingcards/"+xcardP.suit + str(xcardP.rank) + ".gif")
        xcardPlayerImage.draw(gwin)
        self.images.append(xcardPlayerImage)
        
        ycardP = self.deck.dealCard()
        self.pHand.append(ycardP)
        ycardPlayerImage = Image(yposP,"playingcards/"+ycardP.suit + str(ycardP.rank) + ".gif")
        ycardPlayerImage.draw(gwin)
        self.images.append(ycardPlayerImage)

    def hit(self, gwin,xPos,yPos):
        """adds a new card to the player's hand and places it at xPos, yPos"""
        hitCard = self.deck.dealCard()
        self.pHand.append(hitCard)
        hitCardImage = Image(Point(xPos,yPos),"playingcards/"+hitCard.suit + str(hitCard.rank) + ".gif")       
        hitCardImage.draw(gwin)
        self.images.append(hitCardImage)        
        return self.pHand

    def Dealerhit(self,gwin,xPos2,yPos2):
        hitCard = self.deck.dealCard()
        self.dHand.append(hitCard)
        hitCardImage = Image(Point(xPos2,yPos2),"playingcards/"+hitCard.suit + str(hitCard.rank) + ".gif")       
        hitCardImage.draw(gwin)
        self.images.append(hitCardImage)        
        return self.dHand
    
    def evaluateHand(self, hand):
        """totals the cards in the hand that is passed in and returns total
        (ace counts as 11 if doing so allows total to stay under 21)"""
        Total = 0
        hasAce = False
        useAce = False
        for x in hand:
            if x.BJValue() == 1:
                hasAce = True
            Total = Total + x.BJValue()
            if hasAce == True:
                if 17<=(Total+10)<=21:
                    Total = Total + 10
                    useAce = True
            if useAce == True:
                if Total > 21:
                    Total = Total - 10
                    useAce = False
        return Total    
    def emptyHands(self):
        self.pHand = []
        self.dHand = []
    def deleteImages(self):
        for i in self.images:
            i.undraw()
        self.images = []
    def substract(self,amount):
        self.bank -= amount
        return self.bank
    def add(self,amount):
        self.bank += amount
        return self.bank
def main():
    #creates graphical window which the class and its objects will be projected onto
    gwin = GraphWin("Blackjack", 800,700)
    #background of graphical window is now green
    BJ_background = Image(Point(400,350),"playingcards/background.gif")
    BJ_background.draw(gwin)
    #Bank image
    bankImage = Image(Point(400,362.5),"playingcards/bank.gif")
    bankImage.draw(gwin)
    #Bet Image
    betImage = Image(Point(400,596),"playingcards/bet.gif")
    betImage.draw(gwin)
    #GUI Header
    Intro = Text(Point(400,75),"BlackJack")
    Intro.setStyle("bold")
    Intro.setFill("orange")
    Intro.setSize(25)
    Intro.draw(gwin)
    #Button Tab
    buttonTab = Button(gwin,Point(400,672.5),804,60,"")
    #draw deal button
    dealButton = Button(gwin,Point(50,672.5),75,40,"Deal")
    dealButton.activate()
    #draw - stake button
    lStakeButton = Button(gwin,Point(312.5,672.5),75,40,"<<Stake")
    lStakeButton.activate()
    #draw + stake button
    hStakeButton = Button(gwin,Point(400,672.5),75,40,"Stake>>")
    hStakeButton.activate()    
    #draw the hit button
    hitButton = Button(gwin,Point(137.5, 672.5), 75, 40, "Hit")
    hitButton.deactivate()   
    #draw the stand button
    standButton = Button(gwin, Point(225, 672.5), 75, 40, "Stand")
    standButton.deactivate()
    #draw the quit button
    quitButton = Button(gwin,Point(755, 672.5), 75, 40, "Quit")
    quitButton.activate()
    #draw the add funds button
    fundsButton = Button(gwin,Point(667.5,672.5),75,40,"+ Funds")
    fundsButton.deactivate()

    pushText = Text(Point(550,350),"Push!")
    pushText.setStyle("bold italic")
    pushText.setFace("helvetica")
    pushText.setTextColor("lightgray")
    pushText.setSize(15)

    winText = Text(Point(550,350),"You Win!")
    winText.setStyle("bold italic")
    winText.setFace("helvetica")
    winText.setTextColor("white")
    winText.setSize(15)

    loseText = Text(Point(550,350),"You Lose!")
    loseText.setStyle("bold italic")
    loseText.setFace("helvetica")
    loseText.setTextColor("black")
    loseText.setSize(15)

    bustText = Text(Point(550,350),"Busted!")
    bustText.setStyle("bold italic")
    bustText.setFace("helvetica")
    bustText.setTextColor("black")

    xposD = Point(75,235)#center of Dealer's first card
    yposD = Point(150,235)#center of Dealer's second card
    xposP = Point(75,500)#center of Player's first card
    yposP = Point(150,500)#center of Player's second card

    xPos = 225 #hit Card's x position 
    yPos = 500 #hit Card's y position

    xPos2 = 225
    yPos2 = 235

    xPos2 = 225
    yPos2 = 235

    pText = Text(Point(85,437.5),"Player Total:")
    pText.setFill("white")
    pText.setSize(12)
    pText.draw(gwin)

    pText2 = Text(Point(135,437.5),"")

    dText = Text(Point(85,172.5),"Dealer Total:")
    dText.setFill("white")
    dText.setSize(12)
    dText.draw(gwin)

    dText2 = Text(Point(135,172.5),"")
    
    bet = 1
    betText2 = Text(Point(400,362.5),"$"+str(bet))
    betText2.setFill("black")
    betText2.draw(gwin)
    
    Game = BlackJack()
    bank = Game.getBank()
    bankText = Text(Point(400,596),"$"+str(bank))
    bankText.setFill("black")
    bankText.draw(gwin)
    
    pt = gwin.getMouse()
    endGame = False
    madeBid = False
    while not quitButton.clicked(pt):
        offset = 0       
        if fundsButton.clicked(pt):
            bank = Game.add(50)
            bankText.undraw()
            bankText = Text(Point(400,596),"$"+str(bank))
            bankText.draw(gwin)
            fundsButton.deactivate()
            lStakeButton.activate()
            hStakeButton.activate()
            dealButton.activate()
        if endGame == True:          
            if dealButton.clicked(pt):
                Game.emptyHands()
                Game.deleteImages()
                pText2.undraw()
                dText2.undraw()
                winText.undraw()
                loseText.undraw()
                bustText.undraw()
                pushText.undraw()
                endGame = False
        if hStakeButton.clicked(pt):
            if bet < bank:
                bet+=1
                betText2.undraw()
                betText2 = Text(Point(400,362.5),"$"+str(bet))
                betText2.setFill("black")
                betText2.draw(gwin)
        elif lStakeButton.clicked(pt):
            if bet > 1:
                bet-=1
                betText2.undraw()
                betText2 = Text(Point(400,362.5),"$"+str(bet))
                betText2.setFill("black")
                betText2.draw(gwin)
        if dealButton.clicked(pt):
            #Place Bet
            hStakeButton.deactivate()
            lStakeButton.deactivate()
            Game.initDeal(gwin, xposD, yposD, xposP, yposP)
            coverCard = Image(Point(75,235),"playingcards/b1fv.gif")
            coverCard.draw(gwin)
            dealButton.deactivate()
            hitButton.activate()
            standButton.activate()
            pHand = Game.getpHand()
            pTotal =  Game.evaluateHand(pHand)
            pText2 = Text(Point(135,437.5),str(pTotal))
            pText2.setFill("white")
            pText2.setSize(12)
            pText2.draw(gwin)
                     
            if pTotal == 21:
                coverCard.undraw()
                hitButton.deactivate()
                standButton.deactivate()
                dHand = Game.getdHand()
                dTotal = Game.evaluateHand(dHand)
                dText2 = Text(Point(135,172.5),str(dTotal))
                dText2.setFill("white")
                dText2.setSize(12)
                dText2.draw(gwin)
                endGame = True
                dealButton.activate()
                if dTotal == pTotal:
                    pushText.draw(gwin)
                    bank = Game.getBank()
                else:
                    winText.draw(gwin)
                    #Update Bank
                    bank = Game.add(bet*1.5)
            if endGame == False:                    
                while endGame == False:
                    pt = gwin.getMouse()
                    if quitButton.clicked(pt):
                        gwin.close()
                    elif hitButton.clicked(pt):
                        pText2.undraw()
                        Game.hit(gwin, xPos + offset, yPos)                      
                        pHand = Game.getpHand()
                        pTotal = Game.evaluateHand(pHand) 
                        pText2 = Text(Point(135,437.5),str(pTotal))
                        pText2.setFill("white")
                        pText2.draw(gwin)
                        offset += 75
                        #Player Bust Notice
                        if pTotal > 21:
                            hitButton.deactivate()
                            standButton.deactivate()
                            bustText.draw(gwin)
                            endGame = True
                            dealButton.activate()
                            #Update Bank
                            bank = Game.substract(bet)
                    elif standButton.clicked(pt):
                        coverCard.undraw()
                        dHand = Game.getdHand()
                        dTotal = Game.evaluateHand(dHand)
                        dText2 = Text(Point(135,172.5),str(dTotal))
                        dText2.setFill("white")
                        dText2.draw(gwin)
                        hitButton.deactivate()
                        standButton.deactivate()
                        offset = 0
                        while dTotal < 17: #Dealer draws cards until it score touches 17              
                            dText2.undraw()
                            hand = Game.Dealerhit(gwin,xPos2 + offset, yPos2)
                            offset+=75
                            dHand = Game.getdHand()
                            dTotal = Game.evaluateHand(dHand)
                            dText2 = Text(Point(135,172.5),str(dTotal))
                            dText2.setFill("white")
                            dText2.draw(gwin)
                            
                        hitButton.deactivate()
                        standButton.deactivate()
                        endGame = True
                        dealButton.activate()
                        #Dealer Bust
                        if dTotal > 21:                       
                            winText.draw(gwin)
                            bank = Game.add(bet)
                        elif dTotal < pTotal:                          
                            winText.draw(gwin)
                            bank = Game.add(bet)
                        elif dTotal > pTotal:
                            loseText.draw(gwin)
                            bank = Game.substract(bet)
                        else:
                            pushText.draw(gwin)
            bank = Game.getBank()               
            bankText.undraw()
            bankText = Text(Point(400,596),"$"+str(bank))
            bankText.draw(gwin)
            if bank == 0:
                lStakeButton.deactivate()
                hStakeButton.deactivate()
                fundsButton.activate()
                dealButton.deactivate()
            else:
                lStakeButton.activate()
                hStakeButton.activate() 
            bet = 1
            betText2.undraw()
            betText2 = Text(Point(400,362.5),"$"+str(bet))
            betText2.draw(gwin)
                                                 
        pt = gwin.getMouse()

    gwin.close()    
    
if __name__=="__main__": 
    main()













            
