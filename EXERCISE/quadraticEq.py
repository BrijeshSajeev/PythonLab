import math,cmath
a,b,c=(input("Enter the value of a, b, c : ")).split()
a,b,c=[int(a),int(b),int(c)]
d= (b**2)-(4*a*c)

if(d==0):
    sol1=-b/(2*a)
    sol2=-b/(2*a)
    print("The Roots are real and equal")

elif(d>0):
    sol1=(-b+math.sqrt(d)/(2*a))
    sol2=(b+math.sqrt(d)/(2*a))
    print("The roots are real and Different")
else:
    sol1=(-b-cmath.sqrt(d)/(2*a))
    sol2=(-b+cmath.sqrt(d)/(2*a))
    print('The roots are unreal')

print('{0} and {1}'.format(sol1,sol2))