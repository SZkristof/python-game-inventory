inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'kilmandzsaro': 25}
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
    print ("Inventory:")
    print ("count" + " "*n + "Items' name" + "\n" + "-"*n*3)
    b = max(len(x) for x in inventory)*2
    if order == "count,desc":
        a = sorted(inventory,key=inventory.get, reverse=True)
        for i in a:
            placeholder = ' {count:>5} {item:>' + str(b) + '}'
            print (placeholder.format(count=str(inventory[i]), item=i))
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
def import_inventory(inventory, filename="import_inventory.csv"):
    import csv
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            import_inventory = (row)
            for i in import_inventory:
                if i in inventory:
                    inventory[i] += 1
                else:
                    inventory.update({i:1})
    pass


def export_inventory(inventory, filename="export_inventory.csv"):
    import csv

    with open('export_inventory.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(inventory)
    pass
'''
#import_inventory(inventory, filename="test_inventory.csv")
add_to_inventory(inventory, dragon_loot)
print_table(inventory, "count,desc")
#export_inventory(inventory, filename="test_inventory_export.csv")
