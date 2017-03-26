import csv



inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']



def display_inventory(inventory):
    for k, v in inventory.items():
        print (v, k)



def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i:1})



def print_table(inventory, order=None):   
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
    print("Total number of items: " + str(sum(inventory.values())) + "\n") 



def import_inventory(inventory, filename):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            import_inventory = (row)
            for i in import_inventory:
                if i in inventory:
                    inventory[i] += 1
                else:
                    inventory.update({i:1})



def export_inventory(inventory, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(inventory)



import_inventory(inventory, filename="test_inventory.csv")
add_to_inventory(inventory, dragon_loot)
print_table(inventory, "count,desc")
export_inventory(inventory,filename="test_inventory_export.csv")