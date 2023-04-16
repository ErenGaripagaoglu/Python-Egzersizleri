def factorial(a):
    f=1
    if a==0 or a==1:
        f=1
    else:
        for i in range(1,a+1):
            f=f*i
    print(f)