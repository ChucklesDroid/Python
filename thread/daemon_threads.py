#  Daemon threads are threads that run in the background and are not important for running the program. 
#  Your program will not wait for completion of the daemon thread before exiting Non daemon threads normally cannot be killed they stay alive to complete their task


import threading
import time

def counter():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print("Logged in for "+ str(count)+ " secs")

        

thread1 = threading.Thread( target=counter, name="counter", daemon=True, args=() )
#  To set a thread to daemon thread:- ( NOTE:- needs to be done before using start() method )
#  thread1.daemon=True

#  To check if a thread is daemon
if thread1.daemon == True:
    print("True")

#  Both setDaemon() and isDaemon() are deprecated getter and setter functions since Python 3.1


thread1.start()

input("Do you want to quit ?:")
