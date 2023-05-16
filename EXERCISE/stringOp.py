def strlen(str):
    count=0
    while str[count:]:
        count = count+1
    return count
def strrev(str):
    newStr=''
    l=strlen(str)-1
    while(l>=0):
        newStr=newStr+str[l]
        l=l-1
    return newStr
def strcat(str1,str2):
    return str1+str2
def strcmp(str1,str2):
    if(str1==str2):
        print("Both are same")
    elif(str1<str2):
        print(str1+" will come before "+str2)
    else:
        print(str2+" will come before "+str1)
        
print(strlen('Brijesh'))
print(strrev('Brijesh'))
print(strcat('Brijesh ','Sajeev'))
strcmp('Brijesh ','Sajeev')