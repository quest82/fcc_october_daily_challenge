def has_exoplanet(readings):
    import string

    #  Create a dictionary with the exoplanet score
    score_guide = {}
    for index, num in enumerate(list(range(0, 10))):
        score_guide[num] = index
    for index, letter in enumerate(list(string.ascii_uppercase)):
        score_guide[letter] = index + 10


print(has_exoplanet(1)) 


    