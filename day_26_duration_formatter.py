def format(seconds):
    def time_formatter (minu, secs):
        time=['a', 'b']
        if (len(str(minu)) < 2):
            time[0] = f'0{minu}'
        else: 
            time[0] = str(minu)

        if (len(str(secs)) < 2):
            time[1] = f'0{secs}'
        else: 
            time[1] = str(secs)

        return time

    if (seconds // 3600) >= 1:
        hours = seconds // 3600
        remaining_minutes_in_seconds = ((seconds / 60) - (hours * 60)) * 60         # seconds / 60 gives the time in minutes. Removing hours * 60 removes the number of hours leaves only the remaining minutes which is then converted to seconds by * 60.

        minutes = int(remaining_minutes_in_seconds // 60)
        second = int(round(remaining_minutes_in_seconds % 60))
        result_min, result_secs = time_formatter(minutes, second)

        return f'{hours}:{result_min}:{result_secs}'
    else:
        minutes = seconds // 60
        sec = seconds % 60
        _, result_secs = time_formatter(minutes, sec)

        return f'{minutes}:{result_secs}'



print(format(500))
