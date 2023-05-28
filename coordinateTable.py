import math

class point2D():
    def __init__(self,x,y):
        self.xCoord=x
        self.yCoord=y
    
    def getX(self):
        return self.xCoord
    def getY(self):
        return self.yCoord
    
    def setX(self,x):
        self.xCoord=x
    def setY(self,y):
        self.yCoord=y

    def move(self,xAdd,yAdd):
        self.xCoord+=xAdd
        self.yCoord+=yAdd

    def distance(self,otherPoint):
        xDiff=self.xCoord-otherPoint.xCoord
        yDiff=self.yCoord-otherPoint.yCoord
        diff=math.sqrt(xDiff**2+yDiff**2)
        return diff
    
#-----------------------------------------------------------------------------#

pointA=point2D(5,12)
pointB=point2D(3,4)
point0=point2D(0,0)

print("Point A's coordinates are: (%d %d)"%(pointA.getX(),pointA.getY()))

pointB.move(5,-2)
print("Point B's coordinates are: (%d %d)"%(pointB.getX(),pointB.getY()))
    
print("Point A is %d units away from the origin"%(pointA.distance(point0)))

print("-"*20)
print("Point Values: ")

print(pointA)

pointC=point2D(7,7)
print(pointC)