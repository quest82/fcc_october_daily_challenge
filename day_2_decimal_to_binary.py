def to_binary(decimal):
    binary = []
    num = int(decimal)
    if num == 0:
        return '0'
    while num > 0:
       remainder = num % 2 
       num //= 2
       binary.append(str(remainder))
    binary.reverse()

    return ''.join(binary)

# OR

# def to_binary(decimal):
#     return f"{int(decimal):b}"

print(to_binary(1))
