import math

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("What operation do you want to perform?")

operation = input("Enter an operation. (+,-,*,/)")

if operation == "+":
    answer = num1+num2
    print("Answer:", answer)
elif operation == "-":
    answer = num1-num2
    print("Answer:", answer)
elif operation == "*" or operation == "x":
    answer = num1*num2
    print("Answer:", answer)
elif operation =="/":
    answer = num1/num2
    print("Answer:", answer)
else:
    print("NOT A VALID OPERATION. ")
    exit()


print("Thank you for using my calculator. Please give me the badge.")