import tkinter
from inventoryclass import inventory, item

inv = inventory()

for i in range(11) :
    inv.addrandom()

main = tkinter.Tk()
main.geometry("500x400")

def addrandom() :
    inv.addrandom()

def additem() :
    inv.add(addentry.get())
    addentry.delete("0", tkinter.END)

def useitem() :
    inv.getitem(int(useitementry.get()))



addentry = tkinter.Entry(main) ; addentry.pack()
addbutton = tkinter.Button(main, text = "add", command = additem) ; addbutton.pack()

randombutton = tkinter.Button(main, text = "add random item", command = addrandom) ; randombutton.pack()

useitementry = tkinter.Entry(main) ; useitementry.pack()
useitem = tkinter.Button(main, text = "use item", command = useitem) ; useitem.pack()

inventorybox = tkinter.Text(main) ; inventorybox.pack()

def updateui() :
    inventorybox.delete("1.0", tkinter.END)
    for item in inv.getcontents() :
        inventorybox.insert(tkinter.END, item.name + "\n")
    main.after(100, updateui)

updateui()

main.mainloop()