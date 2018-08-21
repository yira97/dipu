import time


def log(*args, **kwargs):
    form = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(form, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)
