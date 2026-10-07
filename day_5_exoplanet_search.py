def has_exoplanet(readings):
    import string

    #  Create a dictionary with the exoplanet score
    score_guide = {}
    for num in range(0, 10):
        score_guide[str(num)] = num
    for index, letter in enumerate(list(string.ascii_uppercase)):
        score_guide[letter] = index + 10

    # Get the readings as numbers
    scores = [score_guide[score] for score in readings]


    # Get threshold of readings
    threshold = (sum(scores) / len(scores)) * 0.8

    return any(score <= threshold for score in scores)
print(has_exoplanet("FREECODECAMP"))


    