def sumGivenNumbers(*n):
    sum = 0
    for i in n:
        sum += i
    print(sum)

sumGivenNumbers(5, 4, 3, 6, 8, 9, 78, 12)