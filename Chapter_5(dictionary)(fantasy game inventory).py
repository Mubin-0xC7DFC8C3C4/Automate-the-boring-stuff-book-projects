import ast

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + " " + str(key))
        item_total += value
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = ast.literal_eval(input())
dragonLoot = ast.literal_eval(input("Enter your dragon loot list: "))

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)