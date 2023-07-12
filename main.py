num1 = 5


num2 = num1

print("num1: ", id(num1))
print("num2: ", id(num2))



num3 = 6

num1 = num3
num2 = num3

print("num1: ", id(num1))
print("num2: ", id(num2))
print("num3: ", id(num3))