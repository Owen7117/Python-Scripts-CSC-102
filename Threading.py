#Threading
#6/6/24
'''
import threading
import time

def thread_function(nameOfThread):
    print(f"thread {nameOfThread}: starting")
    time.sleep(2)
    print(f"Thread {nameOfThread}: finish")
    
print("Main     : before creating thread")
x = threading.Thread(target=thread_function, args=("FirstThread",))
print("Main     : before running thread")
x.start()
print("Main     : wait for the thread to finish")
x.join()
print("Main     : all done")


---------------------------------------------------------------------


from threading import Thread
from time import sleep
from random import randint

class ThreadClass(Thread):
    def __init__(self, name, charToPrint):
        super().__init__(name=name)
        self.charToPrint = charToPrint
    def run(self):
        for i in range(0, 10):
            print(self.charToPrint, end = "")

threadObject1 = ThreadClass("Thread One", 'F')
threadObject1.start()

threadObject2 = ThreadClass("Thread Two", 'A')
threadObject2.start()

threadObject1.join()
threadObject2.join()


---------------------------------------------------------------------


import threading
from time import sleep
def printchar(letter):
    sleep(0.4)
    print(f"{letter}", end = "")
name = "Owen O'Neil"

for letter in name:
    x = threading.Thread(target= printchar, args=(letter,))
    x.start()
   
---------------------------------------------------------------------
'''
import threading
from time import sleep
from time import time
def count_zeros(n):
    start = time()
    count = 0
    for i in range(1, n + 1):#numbers from 1 to input number
        num = i
        while num > 0:
            if num % 10 == 0: 
                count += 1
            num //= 10 #strips right most digit and runs it throught if statement again  
    end = time()
    print("This took {} seconds".format(end - start))
    
def countzeros(given_number):
    start = time()
    count=0
    for i in range(1,given_number + 1):
        count += str(i).count('0')
    end = time()
    print("This took {} seconds".format(end - start))


x = threading.Thread(target = count_zeros, args=(10000000,))
y = threading.Thread(target = countzeros, args=(10000000,))
x.start()
y.start()

