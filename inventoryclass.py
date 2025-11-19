from random import randint
import tkinter

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
    
    def getcontents(self) :
        contentlist = []
        for item in self.contents :
            contentlist.append(item)
        return contentlist

    def getitem(self, index) :
        return self.contents[index]

class item :
    def __init__(self, name) :
        self.name = name

    def use(self) : 
        print("You use " + self.name)