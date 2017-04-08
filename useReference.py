#useReference
def powerSum(power,*args):
	total=0
	for i in args:
		total+=pow(i,power)
	return total
print powerSum(2,3,4)