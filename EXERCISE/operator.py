class Distance:
    def __init__(self,feet,inc):
        self.feet=feet
        self.inch=inc
    
    def __add__(self,p2):
        f=self.feet+p2.feet
        i=self.inch+p2.inch

        return Distance(f,i)
    
    def __gt__(self,p2):
        if(self.feet > p2.feet):
            return True
        elif(self.feet==p2.feet) and(self.inch>p2.inch):
            return True
        else:
            return False

    def display(self):
        print(self.feet,self.inch)
d1=Distance(23,3)
d2=Distance(3,34)
if(d1>d2):
    print("Hello")
else:
    print("Vola")

d3=d1+d2
d3.display()
