# varibale
# variable = value
# Save the value in variable in the format above
# = Unlike the meaning of the symbol, the value is simply stored in a variable.
# Variable can be whatever you want as long as you follow the rules below
# 1. Impossible to start with a number
# 2. Special characters are not possible except the symbol "-"
# 3. No spacing
# 4. Reserved words not possible

# my_name = "Elena"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Data types
# str   -> String       => made up of quotes " "  ' '
# float -> Float        => no quotes and has a decimal point
# int -> integer        => no quotes and no decimal point
# Everbody words (English, Chinese, Korean, etc.) without quotes => error

# a = 10    # saves the integer 10 in the variable a
# b = 'cit'   # saves the string 'cit' in the variable b


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('text or variable or number)
# The print() function prints the 'text', number, or value of 
# the variable inside the bracket and then adds a newline.
# To print multiple items, use a comma (,)
# If you use print() with nothing inside, it prints an empty line

# name = 'Python'
# age = 28
# height = 188
# print(name)
# print()
# print(age)
# print(height)
# print('hi')
# print()
# print(5)
# print(5*10)
# print(name, age, height,"hello")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# inpot('text' or value or variable)
# Displays 'text' or the value of the variable, then waits for keyboard input until enter is pressed
# 'text' or variable can be left out
# variable = input('text' or variable)
# Usually used in this format, without variable it the input value is not saved
# input() always saves the value as a str data type

# var1 = 2
# var2 = input("insert anything:")
# print(var2)
# print(type(var2))

# var2 = int(var2)
# print(type(var2))

# sum = var1 + var2
# print(sum)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Type casting
# str(variable or value)    => converts variable or value to str data types
# float(variable or value)  => converts variable or value to float data types
# int(variable or value)    => converts variable or value to int data type
# Just using them in calculations doesn't change the original varaible's date type
# To change the original variable's data type, save it back into the varibale [ex. a = int(a)]

# var1 = 2
# var2 = '31'
# result = var1 + int(var2)   # saves var1 = var2 converted to int in result
# print(result)
# print(type(var2))   # prints the data type of var2, which is still str
# var2 = int(var2)   # converts var2 to int and saves it back in var2
# print(type(var2))   # prints the new data type of var2


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


var1 = 2025
print('Hello. Enter your name.')
name = input()      #You need to insert the name inside the parenthesis and the parenthesis is empty so it makes sense

print('Welcome', name , 'Enter your age')    # I didnt type the name and I didnt add the string on both sides of the "name"
age = input() 
age = int(age)
year = 2025 - age

print('You were born in' ,year, 'Enter your height')
height = int(input())

two_m = 200 - height
print("There are", two_m, "cm left until 2m.")