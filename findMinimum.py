def findMinimum(list):
    min=list[0]
    for i in range(0, len(list)):
        if (min>list[i]):
            min=list[i]
    return min

array=[10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

arrayMin=findMinimum(array)
print("Minimum value of the array is: ",arrayMin)