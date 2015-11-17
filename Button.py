# Rodrigo
# button.py
# for lab 8 on writing classes

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w #double assignment, gets x max/min from self
        self.ymax, self.ymin = y+h, y-h #double assignment, gets y max/min from self
        p1 = Point(self.xmin, self.ymin)#Creates point 1, top left point of box
        p2 = Point(self.xmax, self.ymax) #creates point 2, bottom right of box
        self.rect = Rectangle(p1,p2) #creates rectangle using the above points
        self.rect.setFill('lightgray') #set-fills the rectangle 
        self.rect.draw(win) #draws rectangle 
        self.label = Text(center, label) #applies label to center of rectangle 
        self.label.draw(win) #draws the label on self
        self.active = True #this variable keeps track of whether or not the button is currently "active"

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgray')##color the text "darkgray"
        self.rect.setWidth(.5)  ##set the outline to look finer/thinner
        self.active = False ##set the boolean variable that tracks "active"-ness to False

    ##check 4.  complete the clicked() method
    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        ##your code here
        #print(p)
        if self.active == True:
            x, y = p.getX(), p.getY()
            #print(x, y)
            if self.xmax >= x >= self.xmin and self.ymin <= y <= self.ymax:
                #print(self.xmin)
                return True
    
if __name__ == "__main__":
    main()
