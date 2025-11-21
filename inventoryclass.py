from random import randint

items = ["sword", "axe", "mace", "rose", "dandelion", "poppy"]

class inventory:
    def __init__(self):
        self.contents = []

    def add(self, name):
        self.contents.append(item(name))

    def addrandom(self) :
        self.contents.append(item(items[randint(0,len(items) - 1)]))

    def remove(self, index):
        self.contents.pop(index)

    def getitem(self, index) :
        return self.contents[index]

class item :
    def __init__(self, name) :
        self.name = name

    def use(self) : 
        return "You use " + self.name