import tkinter
from inventoryclass import inventory, item

inv = inventory()

for i in range(11) :
    inv.addrandom()

main = tkinter.Tk()

def log(message) :
    logbox.insert(tkinter.END, message + "\n")

def addrandom() :
    inv.addrandom()
    log(f"Added {inv.contents[-1].name}")

def additem() :
    inv.add(addentry.get())
    log(f"Added {addentry.get()}")
    addentry.delete("0", tkinter.END)

def useitem() :
    try : 
        print(inv.getitem(int(useitementry.get()) - 1).use())
        log(f"Used {inv.getitem(int(useitementry.get()) - 1).name}")
        
    except ValueError :
        log("Enter a number")

    useitementry.delete("0", tkinter.END)

def remove() :
    try : 
        log(f"Removed {inv.getitem(int(removeentry.get()) - 1).name}")
        inv.remove(int(removeentry.get()) - 1)

    except ValueError :
        log("Enter a number")

    removeentry.delete("0", tkinter.END)

addentry = tkinter.Entry(main) ; addentry.grid(row = 0, column = 0, sticky = "E")
addbutton = tkinter.Button(main, text = "add", command = additem) ; addbutton.grid(row = 0, column = 1, sticky = "W")

randombutton = tkinter.Button(main, text = "add random item", command = addrandom) ; randombutton.grid(row = 0, column = 2, sticky = "W")

useitementry = tkinter.Entry(main) ; useitementry.grid(row = 1, column = 0, sticky="E")
useitem = tkinter.Button(main, text = "use item", command = useitem) ; useitem.grid(row = 1, column = 1, sticky = "W")

removeentry = tkinter.Entry(main) ; removeentry.grid(row = 1, column = 2, sticky = "E")
remove = tkinter.Button(main, text = "remove", command = remove) ; remove.grid(row = 1, column = 3, sticky = "W")

inventorybox = tkinter.Text(main, width = 50) ; inventorybox.grid(row = 3, columnspan = 2)
logbox = tkinter.Text(main, width = 30) ; logbox.grid(row = 3,column = 2, columnspan = 2)

def updateui() :
    inventorybox.delete("1.0", tkinter.END)
    for item in inv.contents :
        inventorybox.insert(tkinter.END, item.name + "\n")
    main.after(100, updateui)

updateui()

main.mainloop()