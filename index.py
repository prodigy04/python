#name ="Prodigy"
#age = "4"
#text ="life is" + name + "hello" +  age + "years old"

#print(text)

#NAIRA TO DOLLAR
#naira = float (input("Enter your naira amount here>>>"))
#rate = float (input("Enter your rate here>>>"))
#dollar = naira/rate

#print(f"The conversion of #{naira} to dollar is ${dollar} using {rate} conversion rate")

#DOLLAR TO NAIRA
#dollar =float(input("Enter your dollar amount here>>>"))
#rate =float(input("Enter your rate here"))
#naira =dollar/rate

#print(f"The conversion of ${dollar} to naira is#{naira} using {rate} conversion rate")


#x=5
#x=x+5
#x +=5
#print(x)


#S.I = P*R*T/100
#P = float(input("Enter your principal>>>"))
#R = float(input("Enter your rate>>>"))
#T = float(input("Enter your time here"))
#S_I = (P*R*T/100)
#print("S.I=", S_I)

#P = int(input("enter your principal>>>"))
#R = int(input("enter your rate>>>"))
#T = int(input("enter your time>>>"))
#S_I =(P*R*T/100)
#print(S_I)

# Python String Class
# name = 'Tuesday'
# print(name)
# print(type(name))
# print(name[3:5])

#To get the number of the word, we must add one,
#to get the number of 'on' in Monday, it will be 1:3, i.e, we must add one to the value not 1,2
#name ='Monday'
#print(name)
#print(type(name))
#print(name[1:3])


#To get the length it starts counting from 1
#name = 'commented'
#print(name)
#print(type(name))
#print(name[0:3])
#print(name[:3])
#print(len(name))

#name ='Hippopotamus'
#print(name)
#print(len(name))

#name ='234567'
#print(name[3])
#print(name[-6:-3])

#comment = """  commented that This is a python class. 
 #        It was started last week and stil continue through this week.
  #       The number of people in this class is   """
#print(comment)
#print(comment[27:39])
#print(comment[0:9])

#String Methods
#print(comment.startswith("commented"))
#print(comment.endswith("is"))
#print(len(comment))

#String () function
#print('length before strip is', len(comment)) 
#calculates with space
#print('length after strip is', len(comment.strip()))
#calculates without space


# val1 = float(input("enter value 1:"))
# val2 = float(input("enter value 2:"))
# name = 'Register User'
# print('''
#   addition
#   subtraction
# '''
# )

# oper = input('enter operation:')
# if oper == name:
#     print(oper)
# else:
#     print('Error')    


# if oper == """   addition""".strip():
#     print(val1 + val2)
# elif oper == 'subtraction':
#     print(val1 - val2)
# else:
#     print('Invalid Selection')   


#multiplication, division, addition, subtraction, modulus(%)
# val1 = float(input("enter value1: "))
# val2 = float(input("enter value2: "))
# print('''
#     addition
#     subtraction
#     multiplication
#     division
#     modulus
# '''
# )

# oper = input('enter operation:')

# if oper == 'addition':
#     print( val1 + val2)
# if oper == 'subtraction':
#     print( val1 - val2)
# if oper == 'multiplication':
#     print( val1 * val2)
# if oper == 'division':
#     print( val1 / val2)
# if oper == 'modulus':
#     print( val1 % val2)

# val3 = float(input("enter value3: "))
# val4 = float(input("enter value4: "))

# print('''
#     addition
#     subtraction
#     multiplication
#     division
#     modulus
# '''
# )

# oper = input('enter operation:')

# if oper == '+':
#     print( val3 + val4)
# if oper == '-':
#     print( val3 - val4)
# if oper == '*':
#     print( val3 * val4)
# if oper == '/':
#     print( val3 / val4)
# if oper == '%':
#     print( val3 % val4)

#Lower() function
# name = 'SUNDAY'
# print(name.lower())
# value = 'method'
# user = input("please enter hello to continue:")
# if value == user.lower():
#     print('welcome')
# else:
#     print("Invalid Input")

#replace() function
# comment = """  commented that This is a python class. It was started
#             last week and still continue through
            # this week. the number of people in this class is    """
# newval = comment.replace("commented", "started")
# print(newval)

#Split() function
# print(comment.split())
# print(comment.split('.'))

#Join() function
# word_split = comment.split()
# print(word_split)
# print(" ".join(word_split))
# value = ["rice", "broccoli","sausage","chocolate"]
# print(value)
# print(" " .join(value))

#Capitalize() function
# comment  = """commented that This is a python class. It was started
#              last week and still continue through
#              this week. the number of people in this class is    """
# print(comment.capitalize())
# print(comment.title())
# paul = "I am coming/n pal"

#Count() function
# print(comment.count("python"))

#In operator
# val = "week" in comment
# print(val)
# val = "weak" not in comment
# print(val)

#Concatination
# name = "paul"
# num = 7

# comment  = f""" {name} commented that This is a python class. It was started
#              last week and still continue through
#              this week. the number of people in this class is {num} """
# print(comment)
# print(comment.format(name,num))

#Escape character
# print('she\'s is the owner paul says and i quote "GOD IS GOOD"')
# print('she is the\b owner\b')

#Array
# list
# tuple
# Set
# dictionary
# list: is a collection which is ordered and changeable
# A list is created with a square bracket[] or list() constructor
# my_list = ["shade", "energy", "magnet", "Charse", "energy"]
# my_list2 = list((12,14, "Sunday", "Charse", True, False,5.08))
# print(my_list)

# print(my_list2)
# for name in my_list:
#     print(name)
# my_list[1] = "solar"
# my_list2[2] = 'paul'
#     print(my_list)
#     print(my_list[2:4])
# my_list.append("tunde")
# print(my_list)
# my_list.insert(-2, "tunde")
# print(my_list)
#Pop to delete

#TRUE IS 1
#FALSE IS 0
#Tuple: A tuple is a collection that is ordered but not changeable. A tuple is created using
#braces i.e() or tuple()
# name = ("Shade", "energy", "magnet", "Charse", "energy")
# name2 = tuple((12, 14, "Sunday", "Charse", True, False, 5.08))
# print(name)
# print(name2)
# print(name[3])
# print(name[-3])
# print(name[-3:-1])
# print(len(name))
# print(type(name2))
# if 1 in name2:
#     print("is available")
# else:
#     print("not available")
# if True in name2:
#     print("is available")
# else:
#     print("not available")
# nm = list(name)
# nm[3] ='wine'
# print(nm)

#Unpacking values of tuple
# item = ("Yam", "Sunday", "Lagos", "Yam", "Sunday", "Lagos", 45)
# (food,name,location,*age) = item
# print(food)
# (food, name, *age, mymy, our) = item
# print(item)
# for na in item:
#     print(na)
# new_name = name + name2
# print(new_name)
# print(name.count("energy"))
# print(name.index("energy"))

# fruits = tuple(('Name', 'name', 'age',12, 'age'))
# print(fruits.index('Name'))

#Set: A set is a collection which is unordered and unindexed. It is written using curly bracket
#i.e {} or set{}
# name = {"Shade", "energy", "magnet", "Charse", "energy"}
# name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# print(name)
# print(name2)
# print(len(name))
# for top in name2:
#     print(top)
# print("magnet" in name)
# print("magnet" not in name)

# name.add("orange")
# print(name)
# name.update(name2)
# print(name)

# e_l =[]
# for i in range(5):
#     inp = input("Enter your amount>>>")
#     e_l.append(inp)
# print(e_l)

#15th of August,2022
# name2 = set((12,14, "Sunday","Charse",True, False,5.08))
# for top in name2:
#         print(top)


# A = []
# B = []
# for i in range(3):
#     a =int(input("Enter your set value:   "))
#     A.append(a)
# for j in range(3):
#     b =int(input("Enter your set value2:   "))
#     B.append(b)
# C = set(A)
# D = set(B)
# print(C)
# print(D)
# E = C.union(D)
# print(E)
# F = C.intersection(D)
# print(F)
# F = C.symmetric_difference(D)
# print(F)
# C.symmetric_difference_update(D)
# print(C)
# C.difference_update(D)
# print(C)
# D.difference_update(C)
# print(D)
# print(C.isdisjoint(D))
# print(C.issubset(D))
# print(D.issuperset(C))
# print(A)
# print(B)
# val1 = {10,11,9,7,8,6}
# val2 = {10,3,4,5,6,12,13,9}
# val3 = val1.intersection(val2)
# print(val3)
# val3 = val1.intersection(val2).intersection(val3)
# val3 = val1.symmetric_difference(val2)
# print(val3)
# val1.symmetric_difference_update(val2)
# print(val1)
# val1.difference_update(val2)
# print(val1)
# print(val1.isdisjoint(val2))
# print(val1.issubset(val2))
# print(val3.issuperset(val1))


#16th of August,2022
# Dictionary: Dictionary is a collection which is ordered, changeable but does not allows
# duplicate and unindexed. Dictionary are used to store data in a key:value pairs
# It is written using {key:value} or (key:value)
# product = { 'producer':'Toyota', 'model':'venza 2021', 'engine':'6 engine', 'color':'black', 'gear':6, "ok":True}
# student_record = dict(name="Tony Johnson", level=300, course="mechanical engineering", subjects=10)
# print(student_record)
# print(product)
# print(len(product))
# print(type(product))
# print(product["model"])
# print(product.get("producer"))
# print(product.keys())
# print(product.values())
# print("6 engine" in product)
# product["color"] =" white"
# print(product)
# product.update({"year":2021, "color":"white"})
# print(product)
# product.pop('color')
# print(product)
#.popitem delete the last item
# product.popitem()
# print(product)
# del product['model']
# print(product)
# for i in student_record:
#     print(student_record[i])
# for x in student_record.values():
#     print(x)
# for x in student_record.keys():
#     print(x)
# for y in student_record.keys():
#     print(y)
# for x,y in student_record.items():
#     print(x, "=", y)
    #   print(f"{x} : {y}")
#dict cant be converted into list, set.
#Dict can only be converted into Dict
# new_record = dict(student_record)
# print(new_record)
# student_details = {
#     "Tony Johnson":{'name':'Tony Johnson', 'level':300, 'location':'Takie', 'dept':'math'},
#     "Micheal Chan":{'name':'Micheal Chan', 'level':200, 'location':'General', 'dept':'Computer'},
#     "Timi Joy": {'level':400, 'location':'Apake', 'dept':'English'}
# }
# std1 =  {'name':"Tony Johnson", 'level':300, 'location':'Takie', 'dept':'math'},
# std2 = {'name':"Micheal Chan", 'level':200, 'location':'General', 'dept':'Computer'}
# student_details2 = {
#     'FIRST PERSON':std1,
#     'SECOND PERSON':std2
# }
# print(student_details2['FIRST PERSON'])
# print(student_details2["Tony Johnson"])
# print(student_details2["Tony Johnson"]['level'])
# for record in student_details2.value():
#         print(record)


#Conditional Statement
#It is used to execute a specific block of code if the given condition is true or false...
#we have:
    # if-Statement,
    # if-else,
    # elif,
    # Nested if and if-else
# If Statement is used for decision making operations, it contains a body of code which only runs when the condition given if Statement is true
# else Statement is usually used when you have to judge one statement on basis of the other
# elif statement is used if the previous condition were not true, then try this next condition

#LOGICAL CONDITION OPERATION
# Equals: ==,
# Not Equals:!=,
# less than: <,
# greater than: >,
# greater than or equal to: >=,
# less than or equal to: <=,
# AND
# OR

#Indentation: python relies on indentation (whitespace at the beginning of a line) to define scope in the code


# x = 50
# if x >= 50:
#     print('Very Good')
# elif x == 50:
#     print('Good')
# else:
#     print('fair')

# Math = int(input('mathematics:'))
# Eng = int(input('english:'))
# Phy = int(input('physics:'))
# Chem = int(input ('chemistry:'))
# total = (Math + Eng + Phy + Chem) / 4
# print(total)
# if total < 45:
#     print('F' + '' + 'FAIL')
# elif total <= 55:
#     print('C'  + ''  + 'GOOD')
# elif total <= 69:
#     print('B' + '' + 'VERY GOOD')
# else:
#     print('A'  + '' + 'EXCELLENT')


#Shorthand if
# a = 30
# b = 44
# print(a) if a > b else print(b)

# time = int(input('Time:'))

# if time < 12:
#     print('GOOD MORNING')
# elif time >= 12:
#     print('GOOD AFTERNOON')
# else:
#     print('GOOD EVENING')

# x = 40

# if x > 20:
#     print('Above 20')
#     if x > 30:
#         print('and above 30')
#     else:
#         print('but not above 30')
# else:
#     print('Not above 20')

# if 'f' in 'food':
#     print('yes')
# else:
#     print('no')


# n = []
# for x in range(2,10):
#     if (x % 2 ==0):
#        n.append(x)
# print(n)

# find the no divisible by 7 and multiple of 5 between 1 and 31


# n =[]
# for x in range(1500, 2701):
#     if (x % 7 == 0) and (x % 5 == 0):
#       n.append(x)
# print(n)

# Temperature Conversion
# Fahrenheit = ( 32f - 32) * 5/9 = 0c
# Celsius = (32c * 9/5) + 32 = 89.6f
# Kelvin = 
# Fahrenheit = float(input("Enter temperature in Fahrenheit:"))
# Celsius = (Fahrenheit - 32) * 5/9
# print(Celsius)


#NAIRA TO DOLLAR
#naira = float (input("Enter your naira amount here>>>"))
#rate = float (input("Enter your rate here>>>"))
#dollar = naira/rate

#print(f"The conversion of #{naira} to dollar is ${dollar} using {rate} conversion rate")
# F = 32 - 212
# k = 0 - 273
# c = 0 - 100
# Fahrenheit = ( 'f' - 32) * 5/9 
# Celsius = ('c '* 9/5) + 32
# inp = (input("Enter the unit you want to convert from:  "))
# inp1 = (input("Enter the unit you want to convert to:  "))
# inp2 = input("Enter the value for temp('c'):")
# val3 = ("Fahrenheit")
# print(f"The conversion of {inp} to Fahrenheit is {val3}")


# Loop
# loop is a statement that conatins instructions that continually repeat until a certain condition is reached
# and with the use of loops we can cut short hundred lines of code to a few...

# e.g
# for x in range(10):
#     print('Hello World')

# Two types of loop:
# for loop and while loop

# A for loop is used for iterating over a sequence(i.e list,a tuple, a dictionary,set, or a string). 
# it can also be used to iterate over a sequence of numbers using range

# looping through a list
# name = ["kola", "bisi", "paul", "gabriel"]
# for x in name:
#     print(x)

# for x in name[-1]:
#     print(x)

# # looping through a string
# for x in "banana":
#     print(x)

#looping through a tuple
# name = tuple((5, "jude","paul", True, 20,10.50))

# for x in name:
#     print(x)

# looping through a dictionary
# product = {'producer':'Toyota', 'model':'venza 2021', 'engine':'6 engine','color':'black','gear':6,"ok":True}  

# for x in product.keys():
#      print(x)
# for x in product.values():
#     print(x)
# for x in product.items():
#     print(x)
# for x,y in product.items():
    # print(x, ":", y)
# using range(number)
# for x in range(5):
        # print(x)
# for x in range(4,10,2):
#     print(x)
# for x in range(3,8,2)
#     print(x)
# 3 is the starting point
# 8 is the ending point
# 2 is the gap
# n = int(input('Enter value for n:'))
# k = int(input('Enter value for k:'))
# for x in range(n,k,5):
#     print(x)

# for j in range(5,k,n): 
#     print(j)


# new = (1,2,3,4)
# for j in new:
#     print(j)
# else:
#     print('no more item')

# Nested for loop
# A nested loop is a loop inside a loop.The inner loop will be executed one time for each iteration of the outer loop.

# pro= ["green", "small","sweet"]

# fruits = ["mango", "orange","cherry"]
# for x in pro:
#     for j in fruits:
#         print(x,j)


# while loop
# while loop continually executes the statement(code) as long as the given condition is True

# n = int(input('>>> '))
# while n <= 10:
#     print('Hello World')
#     break  

# num = 1
# even =[]

# while num <= 10:
#     if num % 2 == 0:
#          even.append(num)
#     num += 1
# print(even)

# even = []

# for i in range(1,10):
#         while i % 2 == 0:
#             even.append(i)
#             break
# print(even)

# count = 0

# while True:
#     print(count)
#     # count += 1
#     if count >= 5:
#         break
#     count += 1
# if we put += 1 here that means we want to add 10 to the output
# print(count): if we put print here that means we want to remove 0 from the output

# Pass
# pass statement is used when we want to do nothing when the condition is met.
# It doesnt skip or stop the execution

