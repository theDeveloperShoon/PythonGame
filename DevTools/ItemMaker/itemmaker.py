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

        if not jsonDataExists():
            self.itemList = ItemList()

            # Sends debug message that file exists
            print("Json file doesn't exist")


# Side Code
items = ItemList()
item1 = Item()
items.items.append(item1)
items.items.append(item1)
print(items.toJson())

# Inititalizes Tkinter
root = Tk()

# Initialize ItemMaker
ItemMaker(root)

# Runs the TKinter Loop
root.mainloop()
