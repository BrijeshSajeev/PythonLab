def Largest(l):
    max=l[0]

    for i in l:
        if(i>max):
            max=i
    return max



list=[]
n=7
print("Enter the list data ")
for i in range (n):
    list.append(int(input()))

print("The Largest Number is ",Largest(list))