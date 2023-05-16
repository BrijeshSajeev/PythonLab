import numpy as np
def mul(a,b,r,c):
    c1=[[0 for i in range(0,r)] for i in range(0,c)]

    for i in range(r):
        for j in range(c):
            c1[i][j]=0
            for k in range(c):
                c1[i][j] = c1[i][j] + a[i][k]*b[k][j]
    print(c1)

def mulNumpy(a,b):
    x=np.array(a)
    y=np.array(b)
    print(x@y)



r=int(input("Enter number of rows"))
c=int(input("Enter number of columns"))

a=[]
print("Enter the elements of A :) ")
for i in range(0,r):
    temp=[]
    for j in range(0,c):
        temp.append(int(input()))
    a.append(temp)

print("Enter the elements of B :) ")
b=[[0 for i in range(0,r)] for j in range(0,c)]

for i in range(r):
    for j in range(c):
        b[i][j] = int(input())
print("matrix a")
print(a)
print("matrix b")
print(b)
mul(a,b,r,c)
print("---------------")
mulNumpy(a,b)