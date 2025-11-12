from random import randint

items = ["sword", "axe", "mace", "rose", "dandelion", "poppy"]

class inventory:
    def __init__(self):
        self.contents = []

    def add(self, name):
        self.contents.append(item(name))

    def addrandom(self) :
        self.contents.append(item(items[randint(0,len(items) - 1)]))

    def remove(self, name):
        for item in self.contents :
            if item.name == name :
                self.contents.remove(item)
                return True
        return False
    
    def printcontent(self) :
        contentlist = []
        for item in self.contents :
            contentlist.append(item.name)
        print(contentlist)

class item :
    def __init__(self, name) :
        self.name = name

    def use(self) : 
        print("You use " + self.name)
        


inv = inventory()

i = 0
while i <= 10 :
    inv.addrandom()
    i += 1

inv.printcontent()