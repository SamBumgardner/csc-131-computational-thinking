"""
File: carddemo.py

Displays playing cards in a window.
"""

from tkinter import *
from cards import Card, Deck 

class CardDemo(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Card Demo")
        self.grid()
        self._deck = Deck()
        self._backImage = PhotoImage(file = Card.BACK_NAME)
        self._cardImage = None
        self._imageLabel = Label(self, image = self._backImage)
        self._imageLabel.grid(row = 0, column = 0, rowspan = 3)
        self._textLabel = Label(self, text = "")
        self._textLabel.grid(row = 3, column = 0)

        self._dealButton = Button(self,
                                  text = "Deal",
                                  command = self._deal)
        self._dealButton.grid(row = 0, column = 1)
        self._shuffleButton = Button(self,
                                     text = "Shuffle",
                                     command = self._shuffle)
        self._shuffleButton.grid(row = 1, column = 1)
        self._newButton = Button(self,
                                 text = "New Deck",
                                 command = self._new)
        self._newButton.grid(row = 2, column = 1)

    def _deal(self):
        """If the deck is not empty, deals and displays the
        next card.  Otherwise, returns the program to its
        initial state."""
        card = self._deck.deal()
        if card != None:
            self._cardImage = PhotoImage(file = card.fileName)
            self._imageLabel["image"] = self._cardImage
            self._textLabel["text"] = str(card)
        else:
            self._new()
            
    def _shuffle(self):
        self._deck.shuffle()
        
    def _new(self):
        """Returns the program to its initial state."""
        self._deck = Deck()
        self._cardImage = None
        self._imageLabel["image"] = self._backImage
        self._textLabel["text"] = ""

def main():
    CardDemo().mainloop()

main()

