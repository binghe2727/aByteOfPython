# -*- coding: utf-8 -*
#multiFunctions.py
def createAdder(x):
	def adder(y):
		return x+y
	return adder
#print adder(10)
add10=createAdder(10)
print createAdder(10)
print add10
add10(3)
print add10