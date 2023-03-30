for i in range(1,100):
    for j in range(2,i):
        if i%j==0:
            print(i, '=' ,j, '*', i//j)
            break
    else:
        print(i,'is a prime number')