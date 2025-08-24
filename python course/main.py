# FUNVTION 

#def greet():
 #    'print a simple greetings.'
 #   print('hello world!')
#greet()
#greet()

  # functions with parameters

#def greet_person(name):
 #   'print a personalized greeting'
  #  print(f"hello,{name}!")

#greet_person('Rooney')
#greet_person('Peter')


# Functions with parameters and a return value

#example1:simple math operation

# def multiply_numbers(x,y):
#    'multiply two numbers and return the result'
#    num1=x
#    num2=y
#    product=x*y
#    print(f"{num1}* {num2}={product}")
# multiply_numbers(5,6)
# multiply_numbers(27,24)
# multiply_numbers(123,245)
# multiply_numbers(15,28)


# #example 2:STRING MANUPULATION

# def format_full_name(first_name,last_name):
#      'take a first and last name and return a formated full name'
#      firstname=first_name
#      secondname=last_name
#      full_namee=first_name + last_name
#      print(f"{first_name}+{last_name}={full_namee}")
#      format_full_name('lovely','joy')
# format_full_name('rooney' 'maina')


#     return result
# print(iterative_factorial(5))

# recursion

# def factorial(n):
#   if n==0:
#         return 1
#   else:
#       return n * factorial(n-1)
  
# print(factorial(8))

 
# def multiply_numbers(x,y):
#   num1=x
#   num2=y
#   product=num1*num2
#   print(f'{num1}*{num2}={product}')
#   multiply_numbers(5,9)

# # COLLECTING USER INPUT
 
# age=input('enter your age:')
# print("You are "+ (str(age)) + "years old") 

# #name=input('enter your name :')
# # print('Hello,'+ name)

# # MODULES

# # import strings

# # print(strings.reverseString('hello'))
# # print(__



num1=float(input('enter first number: '))
num2=float(input('enter second number: '))


total_sum=num1+num2
total_subtraction=num1-num2
total_product=num1*num2
total_quotient=num1/num2
total_square=num1*num1 
total_square1=num2*num2




print(f'{num1}+{num2}={total_sum}')
print(f'{num1}-{num2}={total_subtraction}')
print((f'{num1}*{num2}={total_product} 3') )
print((f'{num1}/{num2}={total_quotient}') ,3) 
print(f'{num1}*{num1}={total_square},{num2}*{num2}={total_square1}')


 