# Comparison operators
# The results of the comparison operation is always True or False
# ==    :   [equal to]
#           True if the same, False is different

# <     :   [less than]
#           True if the right side is larger (excluding equal values), otherwise return False

# >     :   [greater than]
#           True if the left side is larger(excluding equal values), otherwise return False

# <=    :   [less than or equal to]
#           True is the right side is larger or equal, otherwise return False

# >=    :   [greather than or equal to]
#           True if the left side is larger or equal, otherwise return False

# print(5 !=2)
# print(5 < 2)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# if(conditinon) :
#  Run if the above condition is True.
# elif(condition) :
#  Run elif the above condition is True.
# else:
#  Run if all condition are False.

# if    : always use 1
# elif  : use range 0 - infinity
# else  :use 0 or 1
# if can be used by nesting within if.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 100 - 90  : A
# 89 - 70   : B
# 69 - 60   : C
# 59 -      : D

# score = int(input())

# if(100 >= score >= 90) :
#     print('A')
# elif(89>= score >=70):
#     print('B')
# elif(69 >= score >=60):
#     print('C')
# elif(59 >= score >= 0):
#     print ('D')

# print('End')


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

print("Enter number.")
score = int(input())

if(score % 2 == 0) :              #I couldnt do it because I didnt put do the remainder (%) at first
    print("even")                 # I should focus more on the operations like the remainder (%) and the (==) to get the coding

if(score % 2 == 1) :              
    print ('odd')
