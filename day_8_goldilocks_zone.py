from math import sqrt

def goldilocks_zone(mass):
    luminosity = sqrt(pow(mass, 3.5))
    start = round(.95 * luminosity, 2)
    end = round(1.37 * luminosity, 2)
    return [start, end]

print(goldilocks_zone(6))