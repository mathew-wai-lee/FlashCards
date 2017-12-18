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

def ans():
    with open("../Acronyms.json", 'r') as fh:
        temp = json.load(fh)
        sdef.set(temp[sacro.get()])

def Next():
    with open("../Acronyms.json", 'r') as fh:
            temp = json.load(fh)
            ansset = random.choice(list(temp))
            sacro.set(ansset)
            sdef.set("")


# bi = tkinter.Button(root, command = start, text = "Refresh")
bans = tkinter.Button(root, text="Show Ans", command = ans)
bnext = tkinter.Button(root, text = "Next", command = Next)

lacro.pack()
ldef.pack()
bans.pack()
bnext.pack()

tkinter.mainloop()
