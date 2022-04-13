from multiprocessing import process
import os
import time

def square_numbers():
    for i in range(100):
        i * i

processes = []
num_processes = os.cpu_count()
for i in range(num_processes):
    p = process(target= square_numbers)
    processes.append(p)

for p in processes:
    p.start()

for p in processes:
    p.join()