# arithmetic operators
number=int(input("Enter the first number"))
number2=int(input("Enter the second number"))
print(number+number2)
print(number-number2)
print(number*number2)
print(number/number2)
print(number%number2)
# comparison operators
number3=int(input("enter the first number:"))
number4=int(input("enter the second number:"))
print(f"{number3} is equal to {number4}: {number3==number4}")
print(f"{number3} is not equal to {number4}: {number3 != number4}")
print(f"{number3} is greater than {number4}: {number3 > number4}")
print(f"{number3} is less than {number4}: {number3 < number4}")
print(f"{number3} is less than or equals to {number4}: {number3 <= number4}")
print(f"{number3} is greater than or equal to {number4}: {number3 >= number4}")

number5=int(input("enter the fifth number"))
number6=int(input("enter the sixth number"))

print(f"both statements should be true {number5==number6 and number5>number6}")
print(f"one statement should be true {number5==9 or number5>number6}")
