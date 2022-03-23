import json


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
