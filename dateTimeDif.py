#-------------------------------------------#

def bubbleSort(list):
    n=len(list)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if (list[j] > list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
        print(list)

#-------------------------------------------#

import datetime
import random

array=[10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

for i in range(0,1000):
    array.append(random.randint(10,100))

start=datetime.datetime.now()
print("Input: ",end="")
print(array)

print("Sorted Output: ",end="")
bubbleSort(array)

end=datetime.datetime.now()
timeDifferance=end-start
print("Bubble Sort Runtime: ", timeDifferance.microseconds/10**5, "seconds.")

#-------------------------------------------#