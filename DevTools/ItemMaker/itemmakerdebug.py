from tkinter import *

root = Tk()

root.title("ItemMaker")
root.geometry('600x600')

testFrame = Frame(root)
testFrame.grid(column=0,row=0)

tmpList = ["Test", "Test2", "Test3", "Test4"]

testStringVar = StringVar(value=tmpList)

itemsBox = Listbox(testFrame, height=10,
                   listvariable=testStringVar).grid(column=1, row=1)

root.mainloop()
