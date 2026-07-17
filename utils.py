import time


def now():

    return int(time.time())


def human_time(timestamp):

    return time.strftime(
        "%d/%m/%Y %H:%M:%S",
        time.localtime(timestamp)
    )
