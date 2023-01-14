# ===================================================
# Author    :  duzt
# Date      :  2023-1-14
# Descript  :  Python decorator example, sum()
# ===================================================

# define a decorator
def prettyplus(message):
    def pretty(func):
        def inner(*num):
            print(message, f"{num} = ", end='')
            func(*num)
        return inner
    return pretty

# Pass message to decorator
# first run prettyplus, then return pretty
# equal to @pretty, with message passed
@prettyplus(message="sum")
def sum(*num):
    s = 0
    for i in num:
        s += i
    print(s)

# args length unlimited
sum(2, 3, 4 ,5)
