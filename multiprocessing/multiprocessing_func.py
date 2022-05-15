#  Multi processing:- running tasks in parallel on different cpu cores, bypasses GIL used for threading
                #  multi-processing:- better for cpu bound tasks( heavy cpu usage )
                #  multi-threading:- better for i/o bound tasks( waiting around )

from multiprocessing import Process, cpu_count
import time


def counter( num ):
    count = 0
    while (count <= num) :
        count += 1

process1 = Process(target=counter, name="Process1", args=(500000000, ))
process1.start()

process2 = Process(target=counter, name="Process2", args=(500000000, ))
process2.start()

process1.join()
process2.join()

print(time.perf_counter())
