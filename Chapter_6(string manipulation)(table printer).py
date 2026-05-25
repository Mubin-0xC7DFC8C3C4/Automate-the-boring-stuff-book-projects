def printTable(data):
    colwidths = [0] * len(data)
    for i in range(len(data)):
        colwidths[i] = len(max(data[i], key=len))
    
    num_rows = len(data[0])
    num_cols = len(data)

    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(data[col]):
                print(data[col][row].rjust(colwidths[col]), end=' ')
            else:
                print(" " * colwidths[col], end=' ')
        print()

tableData = []
print("Enter lists, seperated by commas")
print("When finished, write 'done'")

while True:
    user_input = input("-> ")
    if user_input.strip().lower() == "done":
        break
    item_list = [obj.strip().replace("'", "") for obj in user_input.split(",")]
    tableData.append(item_list)

if tableData:   
    printTable(tableData)
