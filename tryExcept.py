#Allow only interger value
num1 = 23
num2 = 10


try:
    print("addition is",int(num1)+int(num2))

except Exception as e:
    print(e)