import datetime

def num_seconds_to_next_time_delta(mininterval):
    legal_range = range(1,61)
    if mininterval not in legal_range or 60 % mininterval != 0:
        return 0

    second_interval = mininterval * 60
    now = datetime.datetime.now()
    seconds = second_interval - ((now.minute * 60 + now.second) % second_interval)
    return seconds