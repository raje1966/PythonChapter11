from threading import thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i

threads = []
num_threads = os.cpu_count()
for i in range(num_threads):
    t = thread(target = square_numbers)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()