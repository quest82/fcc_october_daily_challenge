def sequence(n):
    # 1. Make a list with a range starting with 1.
    nums = map(lambda s: str(s), range(1, n + 1))

    # 2. Convert list to a string.

    return "".join(nums)

print(sequence(5))