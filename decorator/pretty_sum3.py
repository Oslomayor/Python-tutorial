# ===================================================
# Author    :  duzt
# Date      :  2023-1-14
# Descript  :  Python decorator example, with parameter
# ===================================================

# define a decorator with parameter
def prettyplus(message):
    def pretty(func):
        def inner(a, b):
            print(message)
            print(f'{a} + {b} = ', end='')
            func(a, b)
        return inner
    return pretty

# Pass message to decorator
# first run prettyplus, then return pretty
# equal to @pretty, with message passed
@prettyplus(message="Hello")
def sumab(a, b):
    print(a + b)

# prints:
# Hello
# 2 + 3 = 5
sumab(2, 3)
