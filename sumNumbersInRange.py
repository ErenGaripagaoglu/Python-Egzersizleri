a,b=int(input("Please enter a number to specify a minimum value: ")),int(input("Please enter a number to specify a maximum value: "))

counter=0
sum=0
for i in range(a,b):
    counter+=1
    sum+=i
    avg=sum//counter
print("Numbers from {} to {}'s sum is: {}. Average is {}".format(a,b,sum,avg))
    