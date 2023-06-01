#-----Twin Prime Numbers-----#

def twinPrimeNumbersInRange(a, b):
    primes=[]
    for x in range(a,b):
        if x > 1:
            for y in range(2, x):
                if (x % y == 0):
                    break
            else:
                primes.append(x)
    
    print("Prime Numbers In Range Are: ", primes)
    print("Twin Prime Numbers In Range Are: ")
    for i in primes:
        twins=[]
        lower = primes[primes.index(i)-1]
        if i - lower == 2:
            twins.append(lower)
            twins.append(i)
            print(twins)
            twins.clear()

#----------------------------#

twinPrimeNumbersInRange(1,100)

#----------------------------#