#Built in function SUM

a = 9
b = 5

c = sum((a,b))
print(sum((5,3)))


def custFunction(a,b):
    """This is our custom function"""
    c =(a+b)
    return c

result=custFunction(50,10)
print("Result==",result)

#Doc string
print(custFunction.__doc__) #This is our custom function