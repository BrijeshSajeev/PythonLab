def febi(n):
    if(n<=1):
        return 1
    else:
        return febi(n-1)+febi(n-2)


print(febi(5))