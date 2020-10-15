class Item:
    def __init__(self, name):
        self.name = name


class Potion(Item):
    def __init__(self, name):
        super().__init__(name)


class Health_potion(Potion):
    def __init__(self, name, heal):
        self.heal = heal
        super().__init__(name)

    def __repr__(self):
        return f'''Health potion "{self.name}". heals for {self.heal} points'''


class Inventory:
    def __init__(self):
        self.items = []

    def __repr__(self):
        if len(self.items) > 0:
            return self.items.__repr__()
        else:
            return '[Inventory is empty]'

    def add_item(self, item):
        if len(self.items) < 6:
            self.items.append(item)
        else:
            print('inventory is full')

    def drop_first_item_by_name(self, name):
        found_item = None
        for i, x in enumerate(self.items):
            if x.name == name:
                found_item = x
                self.items.pop(i)
                break
        if found_item == None:
            print('item is not found')

    def use_item(self, name):
        pass

    def get_passive_bonuses(self):
        pass

#pot = Health_potion('Potion of healing', 50)
