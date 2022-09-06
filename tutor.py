# FUNCTIONAL ARGUMENTS

# def greet():
#     print("Hello World")

#Examples of performed task, print,greet

# greet()


#There are two types of functions 
#1- Performs a task
#2- calculate Returns the value

# def greet(name):
#     # print(f" Hi {name}")
#     return"..."
# # greet("Mosh")
# print(greet("Mosh"))

# def get_greeting(name):
#     return f"Hi {name}"

# message = get_greeting("Mosh")
# print(message)

# # KEYWORD ARGUMENTS
# def increment(number,by):
#     return number + by


# result = increment(2,1)
# print(result)

# #OR

# print(increment(2,1))


#OR

# print(increment(number=2, by =1))
# Square brackets() to create lists and parentheses to create tuples{}
# DEFAULT ARGUMENTS
# optional parameter should come after the required parameter.
# i.e the o.p by=1, should come after the r.p number, another, 
# def increment(number, another,by=1):
#     return number + by

# print(increment(2,4))

# *args, wait, what
# def multipy(*numbers):
#     print(numbers)

# multipy(2,3,4,5)

# def multipy(*numbers):
#     for number in numbers:
#         print(number)
# multipy(2,3,4,5)

# def multipy(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# print(multipy(2,3,4,5))


# **args
# def save_user(**user):
# when we use double asterisks in the parameter,
    # print(user)

# save_user(id=1, name = "John", age = 22)
# we can pass multipe key argument here

# print('o----')
# print('| | | |')
# print('*' * 10)

# name = input("What is your name? ")
# value = input("What is your favorite colour?  ")
# print(name + " " + 'likes' + " " + value)

# WHILE LOOP
# Secret_number = 9
# Guess_count = 0
# Guess_limit = 3
# while Guess_count < Guess_limit:
#     guess = int(input('Guess:  '))
#     Guess_count += 1
#     if guess == Secret_number:
#         print('You Won!')
#         break
# else:
#     print('Sorry, you failed!')

# Class Work
# Car Game
# command = ">>>  "
# while command != "quit":
#     command = input("> ").lower()
#     if command == "start":
#         print("Car Started...")
#     elif command == "stop":
#         print("Car Stopped..")
#     elif command == "help":
#         print("""
#             start - to start the car
#             stop - to stop the car
#             quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that..")
    

# FOR LOOP
# for item in ['Sarah', 'John', 'Mary']:
#     print(item)
# for x in range(3):
#     for y in range(4):
#         print(f'({x}, {y})')

