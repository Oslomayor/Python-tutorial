# ===================================================
# Author    :  duzt
# Date      :  2023-1-14
# Descript  :  Python decorator example, basic usage
# ===================================================

# define a decorator
def pretty(func):
    def inner(*num):
        print(f'{num[0]} + {num[1]} = ', end='')
        func(num[0], num[1])
    return inner

# use the decorator
@pretty
def sumab(a, b):
     print(a + b)


# with @, sumab = pretty(sumab)
# prints
# 2 + 3 = 5
sumab(2, 3)

# equal to 
'''
def sumab(a, b):
     print(a + b)

pretty(sumab)(2, 3)
'''
