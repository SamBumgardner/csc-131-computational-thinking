from tkinter import *

class Counter(Frame):

    def __init__(self):
        """Sets up the window and other stuff."""
        Frame.__init__(self)
        self.master.title("Counter")
        self.grid()

        self._currentCount = 0

        self._labelCounter = Label(self, text = str(self._currentCount))
        self._labelCounter.grid()

        self._buttonCount = Button(self,
                                   text = "Count",
                                   command = self._increaseCount)
        self._buttonCount.grid()
        
        self._buttonReset = Button(self,
                                   text = "Reset",
                                   command = self._resetCount)
        self._buttonReset.grid()

    def _increaseCount(self):
        """Increases current count and updates display"""
        self._currentCount += 1
        self._labelCounter["text"] = str(self._currentCount)

    def _resetCount(self):
        """Resets current count and updates display."""
        self._currentCount = 0
        self._labelCounter["text"] = str(self._currentCount)

def main():
    """Instantiate and pop up the window."""
    Counter().mainloop()

main()
