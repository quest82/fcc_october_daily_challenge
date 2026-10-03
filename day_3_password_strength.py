def check_strength(password):
    strength = 0

    # It is at least 8 characters long.
    if len(password) >= 8:
        strength+=1

    # It contains both uppercase and lowercase letters.
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if has_lower and has_upper:
        strength+=1

    # It contains at least one number.
    has_number = any(char.isdigit() for char in password)

    if has_number:
        strength+=1

    # It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
    special_char = "!@#$%^&*"

    has_specialchar = any(char in special_char for char in password)

    if has_specialchar:
        strength+=1


    comment = ''
    return strength

print(check_strength('1aaaaAa@'))