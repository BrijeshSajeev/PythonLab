def prime(lower,upper):
    
    for num in range (lower,upper+1):
        if num > 1:
            for i in range(2,num):
                if(num % i==0):
                    break
            else:
                print(num)



def primeWhile(lower,upper):
    num=lower

    while(num<=upper):
        if(num > 1):
            for i in range (2,num):
                if(num%i==0):
                    break
            else:
                print(num)
        num = num+1
    

# print(prime(7))   
# print(prime(16))   
print(prime(1,19))   
# print(prime(12))   
# print(prime(23))   
print('-------------')
# print(primeWhile(7))   
# print(primeWhile(16))   
print(primeWhile(1,19))   
# print(primeWhile(12))   
# print(primeWhile(23))   

