def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

print("Enter number:")
while True:
    try:
        num = int(input())
        collatz_result = collatz(num)
        if collatz_result == 1:
            break
    except ValueError:
        print("Error: You must enter an integer")