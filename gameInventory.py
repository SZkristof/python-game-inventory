import operator

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    for first_item, second_item in inventory.items():
        print (second_item, first_item)


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory: #megnézi, 'i' benne van e az inventoryban és ha igen, felveszi az értékét
            inventory[i] += 1
        else:
            inventory.update({i:1})

def print_table(inv, order=None):
    n = max(len(x) for x in inventory)
    print("Inventory:")
    print("count" + " "*n + "Items' name" +"\n" + "-"*n*3)
    b = max(len(x) for x in inventory)*2
    if order == "count,desc":
        a = sorted(inventory, key=inventory.get, reverse=True)
        for i in a:
            placeholder = ' {count:>5} {item:>' + str(b) + '}'
            print(placeholder.format(count=str(inventory[i]), item=i))
    elif order == "count,asc":
        a = sorted(inventory, key=inventory.get)
        for i in a:
            print(str(inventory[i]) + " " + i)
    elif None:
        pass
    else:
        pass
    print("-"*n*3)

'''
def print_table(inventory, order=None):
    n = max(len(x) for x in inventory)
    m = 30-n
    print ("Inventory:" + "\ncount item_name" + "\n" + "-"*m)
    if order == "count,asc":
        a = sorted(inventory, key=inventory.get)
        print (str(inventory[i]) + " "*n + i)
    elif order == "count,desc":
        a = sorted(inventory, key=inventory.get, reverse=True)
        for i in a:
            print(str(inventory[i]) + " "*n + i)
    elif order == None:
        return display_inventory(inventory)
    else:
        print ("You are not worthy to peek into this mighty inventory!")
        pass
'''    

add_to_inventory(inventory, dragon_loot)
print_table(inventory, "count,desc")
# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
