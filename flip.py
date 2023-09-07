import tkinter
import random
import json
import os

try:
    os.chdir(os.getcwd() + '/FlashCards')
except:
    print("Incorrect Directory: " + os.getcwd())

temp = {}

root = tkinter.Tk()

l = tkinter.Label(root, text = "Ready")

sacro = tkinter.StringVar()
lacro = tkinter.Label(root, textvariable = sacro)
sdef = tkinter.StringVar()
ldef = tkinter.Label(root, textvariable = sdef)

with open("Acronyms.json", 'r') as fh:
    temp = json.load(fh)

def ans():
    sdef.set(temp[sacro.get()])

def next():
    ansset = random.choice(list(temp))
    sacro.set(ansset)
    sdef.set("")

def remove():
    del temp[sacro.get()]


bi = tkinter.Button(root, text = "Start!", command = next)
bans = tkinter.Button(root, text="Show Ans", command = ans)
bnext = tkinter.Button(root, text = "Next Prompt (May Return the Same - Keep Clicking)", command = next)
bremove = tkinter.Button(root, text = "Remove Prompt (This Session Only)", command = remove)

lacro.pack(pady=10)
ldef.pack(pady=10)
bnext.pack(pady=(10,1))
bans.pack(pady=(0,10))
bremove.pack(pady=(10,1))
bi.pack(pady=(0,10))

# root.minsize(width=200, height=100)
root.geometry('%dx%d+%d+%d' % (1400, 400, 0, 0))

tkinter.mainloop()
