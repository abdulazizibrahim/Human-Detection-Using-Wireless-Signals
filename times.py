from datetime import datetime
import winsound

def inc_time(time):
    if time[-1:] == '9':
        tenth_min = int(time[-2:-1])
        if tenth_min == 5:
            tenth_min = 0
        else:
            tenth_min = tenth_min + 1
        time = time[:-2] + str(tenth_min) + '0'
    else:
        mins = int(time[-1:])
        mins += 1
        time = time[:-1] + str(mins)
    return time

def current_time():
    current = str(datetime.now())
    current = current[11:-10]
    current = current.strip()
    print(current)
    return current


if __name__ == "__main__":
    time = current_time()
    new_time = inc_time(time)
    while True:
        if new_time == current_time():
            frequency = 5000  # Set Frequency To 2500 Hertz
            duration = 3000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            break