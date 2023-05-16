import math
class Distance:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def distOrigin(self):
        return ((self.x**2)+(self.y**2)+(self.z**2)*0.5)
    
    def distance(self,point):
        diffX=self.x-point.x
        diffY=self.y-point.y
        diffZ=self.z-point.z
        return math.sqrt((diffX**2)+(diffY**2)+(diffZ**3))  
d1=Distance(1,2,3)
d2=Distance(2,3,4)
print(d1.distOrigin())
print(d2.distOrigin())
print(d1.distance(d2))