"""
File: listboxdemo_2.py

Modify listboxdemo.py by attaching an event handler with
a left mouse button release on the listBox widget .
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
        scrollBar = Scrollbar(self._listPane,
                                  orient = VERTICAL)
        scrollBar.grid(row = 0, column = 1,
                           sticky = N+S)

        self.listBox = Listbox(self._listPane,
                                width = 6,
                                height = 10,
                                selectmode = SINGLE)
        
        self.listBox.grid(row = 0, column = 0,
                           sticky = N+S)
        
        scrollBar["command"] = self.listBox.yview
        self.listBox["yscrollcommand"] = scrollBar.set

        # Add some items to the list box and
        # select the first one
        self.listBox.insert(END, "Apple")
        self.listBox.insert(END, "Banana")
        self.listBox.insert(END, "Cherry")
        self.listBox.insert(END, "Orange")
        self.listBox.activate(0)

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
        
        # attach an event handler to the listBox when left mouse button is released
        self.listBox.bind("<ButtonRelease-1>", self._get)

    def _get(self, event):
        """If the list is not empty, copy the selected
         string to the entry field."""
        if self.listBox.size() > 0:
            index = self.listBox.curselection()[0]
            self._inputVar.set(self.listBox.get(index))

    def _add(self):
        """If an input is present, insert it at the
        end of the items in the list box and scroll
        to it."""
        item = self._inputVar.get()
        if item != "":
            self.listBox.insert(END, item)
            self.listBox.see(END)

    def _remove(self):
        """If there are items in the list, removes
        the selected item."""
        if self.listBox.size() > 0:
            self.listBox.delete(ACTIVE)

def main():
    """Instantiate and pop up the window."""
    ListBoxDemo().mainloop()

main()
