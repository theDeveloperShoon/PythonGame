import json


class ItemList:
    def __init__(self):
        self.items = []

    def toJson(self):
        return json.dumps(self, default=lambda x: x.__dict__, indent=4)


class Item:
    def __init__(self):
        self.name = "TestSword"
        self.description = "A test sword"
        self.durability = 100


items = ItemList()
item1 = Item()
items.items.append(item1)
items.items.append(item1)
print(items.toJson())
