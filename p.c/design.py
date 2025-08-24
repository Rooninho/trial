from colorsys import*
from turtle import*
Operator="+ - / *"
Operator=(input("Enter an Operator: "))
num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
if Operator =="+":
    result=num1 + num2
    print(round(result))
elif Operator =="-":
    result=num1 - num2
    print(round(result))
elif Operator =="/":
    result=num1 / num2
    print(round(result ,3))
elif Operator =="*":
    result=num1 * num2
    print(round(result))
else:
    (f"{Operator} is not a valid Operator")

 



