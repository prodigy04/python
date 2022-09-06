# def paul(fname, lname):
#     print(fname + " " + lname)

# paul ("Manny", "Ref")

#Arbitrary Arguments, *args
#If you do not know how many arguements that will be passed into your function, add a * before the parameter name in the function defintion.
#This way the function will receive a tuple of arguments, and can acess the items accordingly:

#Example
#If the number of arguemnts is unknown, add a * before the parameter name:
# def my_function(*kids):
#     print("The oldest child is ", kids[2])

# my_function("Manny","Pete", "Vince")

# def my_function():
#     print("Hello! Hope you are doing well")
# my_function()

# def greet(name):
#     # print("""
#     #     This function greets to
#     #     the person passed in as 
#     #     a parameter
#     # """)
#     print("Hello," + name + " " + "Good Morning!")
# greet("Manny")

#A simple python function to check
#whether x is even or odd


# def evenodd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# #Driver code to call the function
# evenodd(2)
# evenodd(3)
# evenodd(3)
# evenodd(2)
# evenodd(3)

# def first_input(number):
#     begin = []
#     final = []

#     for i in range(5):
#         second_input = int(input(">>>  "))
#         begin.append(second_input)
#         let = second_input * number
#         final.append(let)
        
#     print(final)
# first_input(4)

# def paul():
#     okay = []
#     let = []
#     for i in range(5):
#         value = int(input("Enter>>>  "))
#         okay.append(value)
#         t = okay[0] * value
#         let.append(t)
#     print(let)

# paul()


#Calling a function inside another function

# def Cane():
#     paul()
# Cane()


#Passing a list as an Arguement
#You can send any data types of argument to a function(string, number, list, dictionary etc),
#and it will be treated as the same data type inside the function

#E.g If you send a list as an argument, it will be a list when it reaches the function:


#Example:
# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple","banana","cherry", "mango"]

# my_function(fruits)

#Global Variables
#Variables that are created outisde of a function (as in all of the examples above) are known as global variables
#Global Variables are those which are not defined inside any function and have a global scope

#Global Variables can be used by everyone, both inside of functions and outside.
#Global Variables are accesible throughout the program and inside every function

#Example
#Create a variable outside of a function, and use it inside the function

# x = "awesome"

# def function():
#     print("Python is " + x)

# function()

# x = "awesome"

# def function():
#     x = "fantastic"
#     print("Python is " + x)

# function()


#LOCAL VARIABLES
#Local Variables are those which are defined inside a function and its scope is limited to that function only.
#In other words, we can say that local variables are accessible only inside the function in which it was intialized...

# def f():
#     #local variable
#     s = "I Love Geeks for geeks"
#     print(s)
# f()

# s = "I Love Geeks for geeks"

# def f():
#     #local variable
#     print(s)
# f()

#If we try to use this local variable outside the function:

#Example
# def f():
#     #local variable
#     s = "I Love Geeks for geeks"
#     print("Inside Function:", s)

# #Driver Code
# f()
# print(s)


#There are those which are defined outside any function and which are accessible throughout the program, i.e.,
#inside and outside of every function. Let's see how to create a global variable.

#Example: Defining and accessing global variables


#This function uses global variables
# def f():
#     print("Inside Function:", s)

#     # Global scope
# s = "I love Geeks for geeks"
# f()
# print("Outside function:", s)

# def f():
#     s = "Me too"
#     print(s)
# f()

# #Global Scope
# def f():
#     s = "I love geeks for geeks"
# f()
# print(s)

# a = 1
# #uses global because there is no local 'a'
# def f():
#     print('inside f() : ', a)
# f()

#FUNCTIONAL ARGUMENTS
#You can call a function by using the following types of formal arguments -

#Required arguments
#Keyword arguments
#Default arguments
#Variable-length arguments

#Default Arguments
# A default arguments is a kind of parameter that takes as input a default value if no value is supplied for the argument when the function
#is called. Default arguments are demonstrated in the following instance.

#CODE
# Python code to demonstrate the use of default arguments
# defining a function

# def function(num1, num2 = 40):
#     print("num1 is: ", num1)
#     print("num2 is: ", num2)
# function

# # Calling the function and passing only one arguments
# print("Passing one Argument")
# function(10)


# # Now giving two arguments to the function
# print("Passing two arguments")
# function(10,30)


# #Keyword Arguements
# The arguemnts in a function called are connected to keywords arguemnts.If we provide keyword arguemnts while calling a function,
# the user uses the parameter label to identify which parameter value it is

#Example
# def my_function(child3,child2, child1):
#     print("The youngest child is" + child3)

# my_function(child2 = "Emil",child1 = "Tobias",child3 = "Linus")

#Code
#Python code to demonstrate the use of keyword arguments
#Defining a function
# def function(num1, num2):
#     print("num1 is: ", num1)
#     print("num2 is: ", num2)

# #Calling function and passing arguments without using keyword
# print("without using keyword")
# function(num1 = 30, num2 = 50)

# #Calling function and passing arguments using keyword
# print("with using keyword")
# function(num2 = 50, num1 =30)
# and will override anything in a string''
# the last value will override the value in the first one, 
# print(0 and "5")


# use of return

# m = 5
# def paul():
# def paul(7)
#     return 7 
#     return m  for paul()

# def mike():
#     print(paul() * m)
#     print(paul(7) * m)

# mike()

# m = 5
# n = []

# for i in range(10):
#     n.append(i * m)

# print(n)
