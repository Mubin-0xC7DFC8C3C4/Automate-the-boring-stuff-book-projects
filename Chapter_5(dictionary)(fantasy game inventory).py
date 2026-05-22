import ast

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + " " + str(key))
        item_total = item_total + value
    print("Total number of items: " + str(item_total))

displayInventory(ast.literal_eval(input()))

