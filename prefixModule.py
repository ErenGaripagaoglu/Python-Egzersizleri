class pipFixMath:
    def prefix(self):

        calculation=str(input("Please enter your calculus: "))
        
        try:
            if (int(calculation[0]) in range(0,10) and int(calculation[2]) in range(0,10)): #infix input
                if (len(calculation)==3):
                    prefix=calculation[1]+calculation[0]+calculation[2]
                print(prefix)

        except:
            if (int(calculation[0]) in range(0,10) and int(calculation[1]) in range(0,10)): #postfix input
                if (len(calculation)==3):
                    prefix=calculation[2]+calculation[0]+calculation[1]
                print(prefix)


    
    def infix(self):
        
        calculation=str(input("Please enter your calculus: "))
        
        try:
            if (int(calculation[1]) in range(0,10) and int(calculation[2]) in range(0,10)): #prefix input
                if (len(calculation)==3):
                    prefix=calculation[1]+calculation[0]+calculation[2]
                print(prefix)

        except:
            if (int(calculation[0]) in range(0,10) and int(calculation[1]) in range(0,10)): #postfix input
                if (len(calculation)==3):
                    prefix=calculation[0]+calculation[2]+calculation[1]
                print(prefix)



    def postfix(self):

        calculation=str(input("Please enter your calculus: "))

        try:
            if (int(calculation[1]) in range(0,10) and int(calculation[2]) in range(0,10)): #prefix input
                if (len(calculation)==3):
                    prefix=calculation[1]+calculation[2]+calculation[0]
                print(prefix)

        except:
            if (int(calculation[0]) in range(0,10) and int(calculation[2]) in range(0,10)): #infix input 
                if (len(calculation)==3):
                    prefix=calculation[0]+calculation[2]+calculation[1]
                print(prefix)

######################

calculus=pipFixMath()

calculus.postfix()
calculus.infix()
calculus.prefix()
