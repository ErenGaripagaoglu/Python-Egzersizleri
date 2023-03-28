for i in range(100,1000):
    a=i//100      #By dividing the number to 100 without floating point we can access to hundreds digit
    b=i%100//10   #By taking the modulo of the number, with 100 and diving it w/o float we can access to tenths digit
    c=i%10        #By taking the modulo of the number, with 10 we can access to ones digit
    cubeSum=a**3 + b**3 + c**3 
    if cubeSum == i:
        print("{} is an Armstrong Number.".format(cubeSum))