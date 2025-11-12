class inventory:
    def __init__(self):
        self.contents = []

    def add(self, item, type):
        self.contents.append({"name": item, "type": type})

    def remove(self, name):
        for item in self.contents :
            if item["name"] == name :
                self.contents.remove(item)
                return True
        return False
    
    def printcontent(self, key) :
        name_list = []
        for item in self.contents :
            name_list.append(item[key])
        print(name_list)

inv = inventory()

inv.add("sword", "weapon")

inv.printcontent("name")
inv.printcontent("type")
