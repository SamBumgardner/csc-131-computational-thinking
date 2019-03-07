"""
File: listboxdemo.py

Demonstrates a scrolling list box.
"""

from tkinter import *

class ListBoxDemo(Frame):

    def __init__(self):
        """Manipulating a list box."""
        Frame.__init__(self, bg = "yellow")
        self.master.title("List Box Demo")
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = W+E+N+S)

        # Set up the pane and add the list box and its
        # scroll bar
        self._listPane = Frame(self)
        self._listPane.grid(row = 0, column = 0,
                            sticky = N+S)
        self._yScroll = Scrollbar(self._listPane,
                                  orient = VERTICAL)
        self._yScroll.grid(row = 0, column = 1,
                           sticky = N+S)
        self._theList = Listbox(self._listPane,
                                width = 6,
                                height = 10,
                                selectmode = SINGLE,
                                yscrollcommand = \
                                self._yScroll.set)
        self._theList.grid(row = 0, column = 0,
                           sticky = N+S)
        self._yScroll["command"] = self._theList.yview

        # Add some items to the list box and
        # select the first one
        self._theList.insert(END, "Apple")
        self._theList.insert(END, "Banana")
        self._theList.insert(END, "Cherry")
        self._theList.insert(END, "Orange")
        self._theList.activate(0)

        # Set up the input field and buttons
        self._inputVar = StringVar()
        self._input = Entry(self,
                            textvariable = self._inputVar,
                            width = 6)
        self._input.grid(row = 0, column = 1,
                         sticky = N)
        self._addButton = Button(self,
                                  text = "Add",
                                  command = self._add)
        self._addButton.grid(row = 1, column = 0)
        self._clearButton = Button(self,
                                  text = "Remove",
                                  command = self._remove)
        self._clearButton.grid(row = 1, column = 1)

        # Configure the list pane to expand
        self.rowconfigure(0, weight = 1)
        self._listPane.rowconfigure(0, weight = 1)

    def _add(self):
        """If an input is present, insert it at the
        end of the items in the list box and scroll
        to it."""
        item = self._inputVar.get()
        if item != "":
            self._theList.insert(END, item)
            self._theList.see(END)

    def _remove(self):
        """If there are items in the list, removes
        the selected item."""
        if self._theList.size() > 0:
            self._theList.delete(ACTIVE)

def main():
    """Instantiate and pop up the window."""
    ListBoxDemo().mainloop()

main()
