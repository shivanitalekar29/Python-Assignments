#Design python application which crrates two threads as evenlist and oddlist. Both the threads accept list of integers as aparameter.
#Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all even elements from the list and display the addition. Oddlist thread add all odd elements from input list and display the addtion.

import threading

def evenlist(List):
     count = 0
     for i in List:
         if (i%2==0):
              count = count + i
     print("Addition of even numbers in the list is",count) 
                 
def oddlist(List):
     count = 0
     for i in List:
         if (i%2!=0):
              count = count + i
     print("Addition of odd numbers in the list is",count) 

if __name__=="__main__":
    Data = []
    print("Enter number of elements : ")
    size = int(input())
    
    print("Enter the elements : ")
    for i in range(size):
         Value = int(input())
         Data.append(Value)

    thread1 = threading.Thread(target=evenlist, args=(Data,))
    thread2 = threading.Thread(target=oddlist, args=(Data,))
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()