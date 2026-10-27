def format(seconds):
    if (seconds // 3600) >= 1:
        hours = seconds // 3600
        remaining_minutes_in_seconds = ((seconds / 60) - (hours * 60)) * 60         # seconds / 60 gives the time in minutes. Removing hours * 60 removes the number of hours leaves only the remaining minutes which is then converted to seconds by * 60.

        minutes = int(remaining_minutes_in_seconds // 60)
        second = int(round(remaining_minutes_in_seconds % 60))

        return hours, minutes, second

print(format(4000))
