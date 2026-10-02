def to_decimal(binary):
    #1 Convert str to list
    arr = list(binary)

    #2 Reverse the list so that the index will be able to serve as the power
    decimal = 0
    for index, num in enumerate(reversed(arr)):
        num = int(num)
        digit = num * (2 ** index)
        decimal += digit
    

    return decimal

print(to_decimal("1010101"))