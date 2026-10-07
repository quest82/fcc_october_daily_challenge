def classification(temp):
    if temp >= 30000:
        return "O"
    elif temp >= 10000:
        return 'B'
    elif temp >= 7500:
        return 'A'    
    elif temp >= 6000:
        return 'F'
    elif temp >= 5200:
        return 'G'
    elif temp >= 3700:
        return 'K'
    elif temp >= 0:
        return 'M'
    

print(classification(5778))
    


# "G": 5,200 K - 5,999 K

# "K": 3,700 K - 5,199 K

# "M": 0 K - 3,699 K
