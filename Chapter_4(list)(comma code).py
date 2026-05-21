def list_to_string(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    
    result = ''
    for i in range(len(items)):
        if i == len(items) - 1:
            result += "and " + items[i]
        else:
            result += items[i] + ", "

    return result

input_from_user = input("Enter some items which are seperated by a space or comma: ").split(",")
print(list_to_string(input_from_user))
