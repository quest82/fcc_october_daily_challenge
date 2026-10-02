def to_binary(decimal):
    binary = []
    num = int(decimal)
    while num > 0:
       remainder = num % 2 
       num //= 2
       binary.append(str(remainder))
    binary.reverse()

    return ''.join(binary)

# OR

# def to_binary(decimal):
#     return int(str(decimal), 2)

# print(to_binary(12))
