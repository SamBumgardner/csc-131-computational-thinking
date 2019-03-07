from tkinter import *

def OnClickA(event):
    global counter
    counter += 1
    print("you clicked on", event.widget)
    event.widget["text"] = "Hello " + str(counter)


def OnClickB(event, obj):
    global counter
    counter += 1
    print("you clicked on", obj)
    obj["text"] = "How are you? " + str(counter)

root = Tk()
label1 = Label(root, text="Label 1", bg = "red")
label2 = Label(root, text="Label 2", bg = "green") 
label3 = Label(root, text="Label 3", bg = "blue")
label1.grid()
label2.grid()
label3.grid()

counter = 0 # a counter to increment each time an event handler executes 

label1.bind("<Button-1>", OnClickA)
label2.bind("<Button-1>", lambda event, whichObject = label2: OnClickB(event, whichObject))
label3.bind("<Button-1>", lambda event, whichObject = label3: OnClickB(event, whichObject))

root.mainloop()
