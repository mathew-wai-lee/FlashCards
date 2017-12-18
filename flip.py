import tkinter
import random
import json

temp = {}

root = tkinter.Tk()

l = tkinter.Label(root, text = "Ready")

sacro = tkinter.StringVar()
lacro = tkinter.Label(root, textvariable = sacro)
sdef = tkinter.StringVar()
ldef = tkinter.Label(root, textvariable = sdef)

with open("../Acronyms.json", 'r') as fh:
       temp = json.load(fh)

def ans():
    sdef.set(temp[sacro.get()])

def Next():
    ansset = random.choice(list(temp))
    sacro.set(ansset)
    sdef.set("")

def Remove():
    del temp[sacro.get()]


# bi = tkinter.Button(root, command = start, text = "Refresh")
bans = tkinter.Button(root, text="Show Ans", command = ans)
bnext = tkinter.Button(root, text = "Next", command = Next)
bremove = tkinter.Button(root, text = "Remove", command = Remove)

lacro.pack()
ldef.pack()
bans.pack()
bnext.pack()
bremove.pack()

# root.minsize(width=200, height=100)
root.geometry('%dx%d+%d+%d' % (200, 200, 0, 0))

tkinter.mainloop()
