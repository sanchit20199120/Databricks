
# -----------------INTRO TO PYTHON-----------------------------------------

# Data Types ---------------------------
'''
DATA type in Python -
1. Integer
2. Float
3. String  -- string can concate using + opertor
4. Boolean  ---is a binary data type
5. LIST [] - sequence of items, ordered, mutable, comma separated
6. Dictionary {} - sequence of key value pair , imp. to have all key unique
7. tuples () - immutable, comma separated
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

# Zero parameter
def cad_to_ind():
    print(10 * 61.5)
cad_to_ind()


# One parameter
def cad_to_ind(cad_amount):
    print(cad_amount * 61.5)
cad_to_ind(20)

# Multiple parameter
def cad_to_ind(cad_amount, convertion_rate):
    print(cad_amount * convertion_rate)
cad_to_ind(20,62.5)

def cad_to_ind(cad_amount, convertion_rate):
    print(cad_amount * convertion_rate)
cad_to_ind(cad_amount=20,convertion_rate=62.5)

# Default parameter value
def cad_to_ind(cad_amount, converstion_rate = 65):
    print(cad_amount * converstion_rate)
value_of_function= cad_to_ind(20)
print(value_of_function)

# return
'''our above function runs and print the value 1300 while tthe function body is being executed but when
 we try to have python evalutes a function as an expression, it evalutes to NONE'''

def cad_to_ind(cad_amount, converstion_rate = 65):
    return cad_amount * converstion_rate
value_of_function= cad_to_ind(20)   # stores the value calculated by thr function in a variable
print(value_of_function)


# Returns the length of the input
name_list =['sanchit', 'ankit', 'kanika']
print(len(name_list))

# Return Max value
print(max(name_list))


# Help to get document regarding the built-in function
help(max)


# need to learn the concept ---
my_list = [1, 2 , 3 , 4 , 5 ,6]
for i in my_list:
    print(i)
    my_list.remove(i)
print(my_list)

# Methods ---------------------------------------------------------------------------
# String Method -----------------

firstname = 'sanchit'
surname = 'bhardwaj'
print(firstname.upper())
print(firstname.title())
print(firstname.upper() + " " + surname.upper())

# List [] Methods ----------------------------------------------------------------

# append list
num_list = [1,2,3,4,5]
num_list.append(6)  # In-place method
print(num_list)

# concat list

car_list = ['bmw','Audi']
scooter_list = ['Vespa', 'LML']
print(car_list + scooter_list)

# List Indexing

num_list = [1,2,3,4,5,6,7]
print(num_list[0])  # 1
print(num_list[0:])  # [1,2,3,4,5,6,7]
print(num_list[2:5])  # [3,4,5]   start indexing is inclusive and stop index is exclusive
print(num_list[-1])  # 7
print(num_list[-3])  # 5
print(num_list[:])
num_list[0] = 10  # change the value in a list at index 0 from 1 to 10
print(num_list)


# Dictionaries ---------------------------------------------------------------


breakfast_dict = {
    "pancakes": 1,
    "eggs": 2,
    "waffles": 3,
}

print(breakfast_dict)

# get the values from the dictionaries

print(breakfast_dict.get("waffles"))  # get method
print(breakfast_dict["waffles"])  # alternative method to get the value from the dictionary


# adding new key pair value to the dictionary
breakfast_dict["yogurt"] = 10
print(breakfast_dict)

print(breakfast_dict.keys())  # display all the keys in the dictionary

print("yogurt" in breakfast_dict)   # result will be in boolean


# LOOPS --------------------------------------------

# for-loop
for num in range(0, 11):
    print(num)

# example

first_list = list(range(0,11))
final_list =[]

for i in first_list:
    if i > 4:
        final_list.append(i)
    else:
        pass  # do nothing
print(final_list)

# List comprehension
'''
[variable_name for variable_name in list if(boolean condition)]
'''

final_list =[i for i in first_list if(i > 4)]
print(final_list)

final_list =[2*i for i in first_list if(i > 4)]
print(final_list)


# Errors and Exception in Python

'''
In Python, there are mainly two different kinds of errors:
1. Syntax error --code types incorrectly and pythin does not know how to interpret it.

2. Exception -- 

'''

print(1/0)  # example of exception in python the number can not be divided by zero and get ZeroDivisionError





