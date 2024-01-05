
# -----------------INTRO TO PYTHON-----------------------------------------

# Data Types ---------------------------
'''
DATA type in Python -
1. Integer
2. Float
3. String  -- string can concate using + opertor
4. Boolean  ---is a binary data type
'''


# print data type
print(type(1.1))

# integer and float
print(1+1)
print(1.1*2.3)

# String Concat
print("Hello" + " " + "Sanchit")

# Variable -----------------------
''' Variable names are case sensitive'''

age = 32
name = "Sanchit"
print(name +"  "+ "age is" +" " +str(age))

# f'string Formating ------------------------
name = 'Sanchit'
age = 32
print(f"My name is {name} and I am {age} year old")

# if else statement---------------------

a = 0
if a > 1:
    print("a is greater than 1")
elif a == 1:
    print("a=1")
else:
    print("a is less than 1")

user_input = int(input("age:"))

if user_input > 18:
    print("Adult")
elif a == 18:
    print("Majority age")
else:
    print("Child")

# Function -----------------------

number_list =[]
def summission(number):
    number_list.append(number)
summission(20)
print(number_list)

