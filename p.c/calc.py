operator=input("Enter an operator(+ - * /): ")
num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
if operator == "+":
  result=num1 + num2
  print(result)
elif operator == "-":
  result=num1-num2
  print(result)
elif operator =="/":
  result=num1/num2
  print(round(result, 3))
elif operator =="*":
  result=num1*num2
  print(result)
else:
 print(f"{operator} is not defined")


 m