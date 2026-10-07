def has_exoplanet(readings):
    import string

    #  Create a dictionary with the exoplanet score
    score_guide = {}
    for num in range(0, 10):
        score_guide[str(num)] = num
    for index, letter in enumerate(list(string.ascii_uppercase)):
        score_guide[letter] = index + 10

    # Get average of readings
    sum = 0
    for char in readings:
        sum += score_guide[char]
    average = sum/len(readings) * 0.8
    print(average)
has_exoplanet("9AB98AB9BC98A")


    