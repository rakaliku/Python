num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))

print(num1)
print(num2)

def absolute_value(n):
    if n<0:
        n= -n
    return n
if absolute_value(num1) == absolute_value(num2):
    print("absolute_value of",num1,"and","absolute value of ",num2,"are equal")
else:
    print("both are not equal")
