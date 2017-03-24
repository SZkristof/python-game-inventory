inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    item_total=0
    for k, v in inventory.items():
        print(v, k)
    print ("Total number of items:  " + str(sum(inventory.values())))



def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i:1})


def print_table(inv, order=None):
    b = max(len(x) for x in inv) + 5
    print("Inventory:")
    count = "count".ljust(10," ")
    print(f'{count:>8}'+'Item name'.rjust(b-7, " "))
    asdf = []
    for i in inventory:
        asdf.append(inventory[i])
    c = len(str(max(asdf)))
    print('-'*(b+c+1))
    if order == "count,desc":
        a = sorted(inventory, key=inventory.get, reverse=True)
        for i in a:
            placeholder = '{count:>{0}} {item:>' + str(b) + '}'
            print(placeholder.format(str(c),count=str(inventory[i]), item=i))
        print('-'*(b+c+1))
        print ("Total number of items:  " + str(sum(inventory.values())))
    elif order == "count,asc":
        a = sorted(inventory, key=inventory.get)
        for i in a:
            print(str(inventory[i]) + " " + i)
        print('-'*(b+c+1))
        print ("Total number of items:  " + str(sum(inventory.values())))
    elif None:
        pass
    else:
        pass

def import_inventory(inventory, filename="test_inventory.csv"):
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


add_to_inventory(inventory, dragon_loot)
print_table(inventory, "count,desc")
import_inventory(inventory)
export_inventory(inventory)
