import json
import os
from tkinter import *
from tkinter import ttk


# Checks if the json data exists
def jsonDataExists():
    return os.path.isfile("Data/itemlist.json")


# Defining ItemList class
class ItemList:
    def __init__(self):
        self.items = []

    def toJson(self):
        return json.dumps(self, default=lambda x: x.__dict__, indent=4)


# Defining Item Class
class Item:
    def __init__(self):
        self.name = "TestSword"
        self.description = "A test sword"
        self.durability = 100


# Defining ItemMaker Class
class ItemMaker():

    # Defining Constructor
    def __init__(self, root):
        self.root = root
        self.root.title("ItemMaker")
        self.root.geometry('600x600')

        self.mainframe = Frame(self.root)
        self.mainframe.grid(column=0, row=0)

        if jsonDataExists():
            self.itemList = ItemList()
            print("Json File Exists")
        else:
            self.itemList = ItemList()
            tmpItem = Item()
            tmpItem2 = Item()
            tmpItem2.name = "TestSword2"
            self.itemList.items.append(tmpItem)
            self.itemList.items.append(tmpItem2)

            # Sends debug message that file exists
            print("Json file doesn't exist")

        self.tmpList = []
        for item in self.itemList.items:
            self.tmpList.append(item.name)

        print(self.tmpList)

        self.stringVar = StringVar(value=self.tmpList)

        self.itemsBox = Listbox(
            self.mainframe, listvariable=self.stringVar).grid(column=1, row=1)


# Side Code
# items = ItemList()
# item1 = Item()
# items.items.append(item1)
# items.items.append(item1)
# print(items.toJson())

# Inititalizes Tkinter
root = Tk()

# Initialize ItemMaker
ItemMaker(root)

# Runs the TKinter Loop
root.mainloop()
