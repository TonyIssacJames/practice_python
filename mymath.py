'''
Module name: mymath
Description: It inculudes math functions
'''

version = 1.2

print(".........  my math version = ", version)

def add1(*args):
	sum =  0
	for arg in args:
		sum += arg

	return sum
