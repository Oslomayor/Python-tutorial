# ===================================================
# Author    :  duzt
# Date      :  2023-1-14
# Descript  :  Python decorator example, original version
# ===================================================

def pretty(func):
	def inner(a, b):
		print(f'{a} + {b} = ', end='')
		func(a, b)
	return inner

def sumab(a, b):
     print(a + b)

# prints
# 2 + 3 = 5
pretty(sumab)(2, 3)
