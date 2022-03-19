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

    def removeItem(self, index):
        self.items.pop(index)

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
        self.root.configure(background='red')

        self.root.rowconfigure(0, weight=3)

        # Works on the menu bar
        self.root.option_add('*tearOff', False)
        self.menuBar = Menu(self.root)
        self.root['menu'] = self.menuBar
        self.menuFile = Menu(self.menuBar)
        self.menuDebug = Menu(self.menuBar)
        self.menuBar.add_cascade(menu=self.menuFile, label="File")
        self.menuBar.add_cascade(menu=self.menuDebug, label="Debug")

        self.menuFile.add_command(label='New Item', command=self.newItem)
        self.menuFile.add_command(label='Remove Item', command=self.removeItem)

        self.menuDebug.add_command(
            label='Print Index', command=self.debugSelectedIndex)

        # Checks if the Json File Exists (Will be removed)
        if jsonDataExists():
            self.itemList = ItemList()
            print("Json File Exists")
        else:
            self.itemList = ItemList()
            tmpItem = Item()
            self.itemList.append(tmpItem)

        self.nameList = []
        for item in self.itemList.getItems():
            self.nameList.append(item.name)

        print(self.nameList)

        self.stringVar = StringVar(value=self.nameList)

        self.itemBox = Listbox(
            self.mainframe, listvariable=self.stringVar)
        self.itemBox.grid(column=1, row=1)

        # self.itemBox.bind('<Double-1>', itemBoxSelection())

    def newItem(self):
        newitem = Item()
        self.itemList.append(newitem)
        self.updateListbox()

    def updateListbox(self):
        self.nameList = []
        for item in self.itemList.getItems():
            self.nameList.append(item.name)

        print(self.nameList)

        self.stringVar.set(self.nameList)
        # self.itemsBox = self.stringVar

    def debugSelectedIndex(self):
        print(self.itemBox.curselection())

    def removeItem(self):
        for item in self.itemBox.curselection():
            index = item
            self.itemList.removeItem(index)
        self.updateListbox()


# Test to see if .toJson function of itemList works
"""
items = ItemList()
item1 = Item()
items.items.append(item1)
items.items.append(item1)
print(items.toJson())
"""

# Inititalizes Tkinter
root = Tk()

# Initialize ItemMaker
ItemMaker(root)

# Runs the TKinter Loop
root.mainloop()
