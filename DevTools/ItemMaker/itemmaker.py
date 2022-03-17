import json
import os
from tkinter import *
from tkinter import ttk


# Checks if the json data exists
def jsonDataExists():
    return os.path.isfile("Data/itemlist.json")


# Defining ItemList class
class ItemList:
    # Defining Constructor
    def __init__(self):
        self.items = []

    # Makes it 'nicer' to append items
    def append(self, item):
        self.items.append(item)

    # Returns the items in the list
    def getItems(self):
        return self.items

    # Converts the item list to json
    def toJson(self):
        return json.dumps(self, default=lambda x: x.__dict__, indent=4)


# Defining Item Class
class Item:
    # Defining Constructor
    def __init__(self):
        # Defines class variables
        self.name = "NewItem"
        self.description = "A new item"
        self.durability = 100


# Defining ItemMaker Class
class ItemMaker():

    # Defining Constructor
    def __init__(self, root):

        self.root = root

        # Does root modifications
        self.root.title("ItemMaker")
        self.root.geometry('600x600')

        # Creates a frame
        self.mainframe = Frame(self.root)
        self.mainframe.grid(column=0, row=0)

        # Works on the menu bar
        self.root.option_add('*tearOff', False)
        self.menuBar = Menu(self.root)
        self.root['menu'] = self.menuBar
        self.menuFile = Menu(self.menuBar)
        self.menuBar.add_cascade(menu=self.menuFile, label="File")
        self.menuFile.add_command(label='New Item', command=self.newItem)

        # Checks if the Json File Exists (Will be removed)
        if jsonDataExists():
            self.itemList = ItemList()
            print("Json File Exists")
        else:
            self.itemList = ItemList()
            tmpItem = Item()
            tmpItem2 = Item()
            tmpItem.name = "TestSword"
            tmpItem2.name = "TestSword2"
            self.itemList.append(tmpItem)
            self.itemList.append(tmpItem2)

        tmpList = []
        for item in self.itemList.getItems():
            tmpList.append(item.name)

        print(tmpList)

        self.stringVar = StringVar(value=tmpList)

        self.itemsBox = Listbox(
            self.mainframe, listvariable=self.stringVar).grid(column=1, row=1)

    def newItem(self):
        newitem = Item()
        self.itemList.append(newitem)
        self.updateListbox()

    def updateListbox(self):
        tmpList = []
        for item in self.itemList.getItems():
            tmpList.append(item.name)

        print(tmpList)

        self.stringVar.set(tmpList)
        self.itemsBox = self.stringVar

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
