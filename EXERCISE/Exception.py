try:
    num1,num2=eval(input("Enter 2 numbers seprated by a comma >> "))
    result=num1/num2

    if(result < 20):
        raise RuntimeError()
except ZeroDivisionError:
    print('Zero cannt be divided')
except SyntaxError:
    print('may be a comma missing')
except RuntimeError:
    print('Some Thing went worng')
except:
    print("OOPS....")
else:
    print("No error")
finally:
    print("Completed ...")