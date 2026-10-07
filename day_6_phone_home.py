def send_message(route):
    # Speed of message = 300,000 km/s
    # time = speed / distance (t = v/s)

    # Get the total no of seconds without delay
    no_delay_time = sum(route) / 300000

    # Add delay
    delayed = no_delay_time + (0.5 * (len(route) - 1))




    return delayed

print(send_message([1000000, 500000000, 1000000]))