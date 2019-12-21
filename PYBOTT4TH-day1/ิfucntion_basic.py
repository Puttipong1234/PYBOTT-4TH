# a= 5
# b= 10
# c = a+b
# print(c)

def add(num1,num2):
    result = num1+num2
    return result

def minus(num1,num2):
    result = num1-num2
    return result

def multi(num1,num2):
    result = num1*num2
    return result

def divide(num1,num2):
    result = num1/num2
    return result

res1 = add(num1=5,num2=6)
res2 = minus(num1=5,num2=6)
res3 = multi(num1=5,num2=6)
res4 = divide(num1=5,num2=6)


print(res1 , res2 , res3 , res4)