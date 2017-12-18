import tkinter 
import json

temp = {}

try:
    with open("../test.json", 'r') as fh:
        temp = json.load(fh)
except:
    pass


def submit():
    with open("../test.json", 'w') as fh:
        
        Acronym = tfAcro.get()
        Definition = tfDef.get()
        temp[Acronym] = Definition
        json.dump(temp, fh, sort_keys=True)
        vAcro.set("")
        vDef.set("")
        tfAcro.focus_set()
        s.set(Acronym)
        lb.delete(0, tkinter.END)
        # lbdef.delete(0, tkinter.END)
        
        for item in list(sorted(temp)):
            lb.insert(tkinter.END, item + " | "+ temp[item])
        
        # for defs in list(sorted(temp)):
            # lbdef.insert(tkinter.END, temp[defs])

        
root = tkinter.Tk()

vAcro =  tkinter.StringVar()
tfAcro = tkinter.Entry(root, textvariable = vAcro)
tfAcro.focus_set()

vDef = tkinter.StringVar()
tfDef = tkinter.Entry(root, textvariable = vDef)

b = tkinter.Button(root, command = submit, text = "Submit")
s = tkinter.StringVar()
l = tkinter.Label(root, textvariable = s)
lb = tkinter.Listbox(root)
# bd = tkinter.Button(root, text="Delete", command=lambda lb=lb: lb.delete(tkinter.ANCHOR))
# lbdef = tkinter.Listbox(root)
sorted(temp)

for item in list(temp):
    lb.insert(tkinter.END, item + " | "+ temp[item])

# for defs in list(temp):
#     lbdef.insert(tkinter.END, temp[defs])

# tfAcro.grid(row= 1, column = 1)
# tfDef.grid(row = 1, column = 2)
# b.grid(row = 1, column = 3)
# l.grid(row  = 1, column = 4)
# lb.grid(row = 2, column = 1, sticky = "NEWS")
# lbdef.grid(row = 2, column = 2, sticky = tkinter.N+tkinter.S)
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
# # # bd.grid(row = 2, column = 3)


tfAcro.pack(side = tkinter.TOP, fill = tkinter.X)
tfDef.pack(side = tkinter.TOP, fill = tkinter.X)
b.pack(side = tkinter.TOP, fill = tkinter.X)
l.pack(fill = tkinter.X)
lb.pack(side = tkinter.LEFT, fill = tkinter.BOTH, expand = 1)
# lbdef.pack(side = tkinter.LEFT, fill = tkinter.BOTH, expand = 1)
# bd.grid(row = 2, column = 3)

root.bind("<Return>", lambda x: submit())

tkinter.mainloop()
