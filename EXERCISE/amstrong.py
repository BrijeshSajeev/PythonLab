def amstrong(n):
    str_no=str(n)
    length=len(str_no)
    ar_sum=0
    for i in str_no:
        ar_sum += int(i)**length

    if (ar_sum==n):
        return True
    else:
        return False

print(amstrong(317))    
print(amstrong(371))    
print(amstrong(153))    
