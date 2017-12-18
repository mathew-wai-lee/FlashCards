import tkinter 
import json

temp = {}

try:
    with open("../Acronyms.json", 'r') as fh:
        temp = json.load(fh)
except:
    pass


###########################Functions#################################################
def submit():
    with open("../Acronyms.json", 'w') as fh:
        
        Acronym = tfAcro.get()
        Definition = tfDef.get()
        temp[Acronym] = Definition
        json.dump(temp, fh, sort_keys=True)
        vAcro.set("")
        vDef.set("")
        tfAcro.focus_set()
        s.set(Acronym)
        lb.delete(0, tkinter.END)
        
        for item in list(sorted(temp)):
            lb.insert(tkinter.END, item + " | "+ temp[item]) 
        

# USED TO ADD A DELETE BUTTON FEATURE - PENDING
# def testbut():

#     result = lb.get("active")
#     print(result.split(" ", 1)[0]) #Extracts the Acronym

###############################Create and define widgets################################
# Create         
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
# testbut = tkinter.Button(root, command = testbut, text = "print")

####################Pre-populate the list##################################################
sorted(temp)

for item in list(temp):
    lb.insert(tkinter.END, item + " | "+ temp[item])

############################ Pack all of the items into the window###############################################
tfAcro.pack(side = tkinter.TOP, fill = tkinter.X)
tfDef.pack(side = tkinter.TOP, fill = tkinter.X)
b.pack(side = tkinter.TOP, fill = tkinter.X)
l.pack(fill = tkinter.X)
lb.pack(side = tkinter.LEFT, fill = tkinter.BOTH, expand = 1)
# testbut.pack()

#Add entry by return key
root.bind("<Return>", lambda x: submit())

#Set minimum Size
# root.minsize(width=300, height = 1000)
root.geometry('%dx%d+%d+%d' % (300, 1000, 0, 0))

#Start loop
tkinter.mainloop()
