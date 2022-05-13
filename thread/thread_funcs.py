import time
import threading


def breakfast():
    time.sleep(3)
    print("You are eating breakfast")

def coffee():
    time.sleep(4)
    print("You drank coffee")

def homework():
    time.sleep(5)
    print("You finished your homework")

#  To create threads we will make use of threading.Thread()
thread1 = threading.Thread(target=breakfast, name="B", args=())
thread2 = threading.Thread(target=coffee, name="C", args=())
thread3 = threading.Thread(target=homework, name="H", args=())
thread1.start(), thread2.start(), thread3.start()   # To start threads 1,2 and 3

#  To make all the threads synchronise with the main thread we will make use of "thread_name".join()
thread1.join(), thread2.join(), thread3.join()

print(threading.active_count())                     # Prints total no of threads both parent and child total
print(threading.enumerate())                        # Prints the name of threads 
print(time.perf_counter())                          # Prints the time taken by main thread to complete execution
