import threading

to_print = 1
cv = threading.Condition(lock=None)


def action(cur, cnt):
    global cv
    global to_print

    for i in range(cnt):
        with cv:
            cv.wait_for(lambda: to_print == cur)
            print(cur, end="", sep="")
            to_print = to_print + 1
            if to_print == 4:
                to_print = 1
            cv.notify(n=3)


def create(threads):
    for i in range(3):
        threads.append(threading.Thread(target=action, args=(i + 1, n)))


def start(threads):
    for thread in threads:
        thread.start()


def join(threads):
    for thread in threads:
        thread.join()


n = int(input())
threads = []

create(threads)
start(threads)
join(threads)
