#Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter. Small thread display number of small character, captial thread siplay number of capital characters and digits thread display number of digits. Display id and name of each thread
import threading
import multiprocessing
import os

def small(str):
    count = 0
    for i in str:
        if i.islower():
            count=count+1
    print("Small letters :",count)
    print('process id of small :',os.getpid)    

def capital(str):
    count = 0
    for i in str:
        if i.isupper():
            count=count+1
    print("Capital letters :",count)

def digit(str):
    count = 0
    for i in str:
        if i.isdigit():
            count=count+1
    print("Digits :",count)

if __name__ == "__main__":
    word = input("Enter the string value : ")

    thread1 = threading.Thread(target=small, args=(word,))
    thread2 = threading.Thread(target=capital, args=(word,))
    thread3 = threading.Thread(target=digit, args=(word,))
    print(os.getpid)

    thread1.start()
    thread2.start()
    thread3.start()