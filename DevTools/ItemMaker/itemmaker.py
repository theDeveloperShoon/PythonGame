import json
import os
import io
from tkinter import *
from tkinter import filedialog
from classes.item import Item
from classes.itemlist import ItemList


# Defining ItemMaker Class
class ItemMaker():

    # Defining Constructor
    def __init__(self, root):

        self.root = root

        # Does root modifications
        self.root.title("ItemMaker")
        self.root.geometry('600x600')

        self.root.configure(background='red')

        self.root.rowconfigure(0, weight=3)
        self.root.columnconfigure(2, weight=3)

        # Works on the menu bar
        self.root.option_add('*tearOff', False)
        self.menuBar = Menu(self.root)
        self.root['menu'] = self.menuBar
        self.menuFile = Menu(self.menuBar)
        self.menuEdit = Menu(self.menuBar)
        self.menuDebug = Menu(self.menuBar)
        self.menuBar.add_cascade(menu=self.menuFile, label="File")
        self.menuBar.add_cascade(menu=self.menuEdit, label='Edit')
        self.menuBar.add_cascade(menu=self.menuDebug, label="Debug")

        self.menuFile.add_command(label='Open', command=self.openFile)
        self.menuFile.add_command(label='Save', command=self.saveFile)

        self.menuEdit.add_command(label='New Item', command=self.newItem)
        self.menuEdit.add_command(
            label='Remove Item', command=self.removeItem)

        self.itemList = ItemList()
        tmpItem = Item()
        self.itemList.append(tmpItem)

        self.nameList = []
        for item in self.itemList.getItems():
            self.nameList.append(item.name)

        self.stringVar = StringVar(value=self.nameList)

        self.itemBox = Listbox(
            self.root, listvariable=self.stringVar)
        self.itemBox.grid(column=0, row=0, sticky=(N, S, W))

        self.listBoxScrollbar = Scrollbar(
            self.root, orient=VERTICAL, command=self.itemBox.yview)
        self.listBoxScrollbar.grid(column=1, row=0, sticky=(N, S))

        self.itemBox.configure(yscrollcommand=self.listBoxScrollbar.set)

        self.frame = Frame(self.root)
        self.frame.grid(column=2, row=0, sticky=(N, S, E, W))
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(1, weight=0)
        self.frame.rowconfigure(2, weight=0)
        self.frame.columnconfigure(0, weight=3)
        self.frame.columnconfigure(1, weight=3)

        # Name Entry
        self.nameLabel = Label(self.frame, text="Name")
        self.nameLabel.grid(column=0, row=0)

        self.nameEntryVariable = StringVar()
        self.nameEntry = Entry(self.frame, textvariable=self.nameEntryVariable)
        self.nameEntry.grid(column=1, row=0)

        # Description Entry
        self.descriptionLabel = Label(self.frame, text='Description')
        self.descriptionLabel.grid(column=0, row=1)

        self.descriptionEntryVariable = StringVar()
        self.descriptionEntry = Entry(
            self.frame, textvariable=self.descriptionEntryVariable)
        self.descriptionEntry.grid(column=1, row=1)

        # Durability Entry
        self.durabilityLabel = Label(self.frame, text='Durability')
        self.durabilityLabel.grid(column=0, row=2)

        self.durabilityEntryVariable = StringVar()
        self.durabilityEntry = Entry(
            self.frame, textvariable=self.durabilityEntryVariable)
        self.durabilityEntry.grid(column=1, row=2)

        # Save Button
        self.saveButton = Button(
            self.frame, text='Save', command=self.saveItem)
        self.saveButton.grid(column=0, row=3, columnspan=2)

        # Binds the itemBox to open the item
        self.itemBox.bind('<Double-1>', self.openItem)
        self.itemBox.bind('<KeyRelease-Delete>', self.removeItem)

        # Sets Current Item open to 0
        self.currentItem = 0

    # Changes the currentItem to the selected item
    def openItem(self, event):
        self.currentItem = self.itemBox.curselection()[0]

        """
        Make it where the properties are the item's properties
        """

    # Saves the entered properties into the item
    def saveItem(self):
        itemID = self.currentItem
        self.itemList.items[itemID]
        self.itemList.items[itemID].name = self.nameEntryVariable.get()
        self.itemList.items[itemID].description = self.descriptionEntry.get()

        self.updateListbox()

    # Creates a new item into the itemList
    def newItem(self):
        newitem = Item()
        self.itemList.append(newitem)
        self.updateListbox()

    # Updates the names of items in the list
    def updateListbox(self):
        self.nameList = []
        for item in self.itemList.getItems():
            self.nameList.append(item.name)

        print(self.nameList)

        self.stringVar.set(self.nameList)

    # Removes the currently selected item from the list
    def removeItem(self, event):
        for item in self.itemBox.curselection():
            index = item
            self.itemList.removeItem(index)
        self.updateListbox()

    # Saves the json file into wherever you ask for it to be stored
    def saveFile(self):
        savedirectory = filedialog.asksaveasfilename(
            filetypes=[('Json', ".json")])
        fileSaving = open(savedirectory+".json", mode='w+')
        fileSaving.write(self.itemList.toJson())

    # Opens the json file specified
    def openFile(self):
        opendirectory = filedialog.askopenfilename(
            filetypes=[('Json', '.json')])
        fileOpened = open(opendirectory, mode="r")

        jsonloaded = json.load(fileOpened)

        tmpItemList = ItemList()
        returnItemList = ItemList()

        tmpItemList.__dict__ = jsonloaded
        for item in tmpItemList.items:
            tmpItem = Item()
            tmpItem.__dict__ = item
            returnItemList.append(tmpItem)

        self.itemList = returnItemList
        self.updateListbox()


# Inititalizes Tkinter
root = Tk()

# Initialize ItemMaker
ItemMaker(root)

# Runs the TKinter Loop
root.mainloop()
