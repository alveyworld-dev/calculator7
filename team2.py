# Ricky Harding, Caden Bringhurst, Josh Jimenez, Brian 

def abs(x):
	"""This function finds the distance X is from 0."""
	if x < 0:
		return x * -1
	else:
		return x

def fact(x):
	
	if x == 0:
		return 1
	elif x < 0:
		return "Not a real number"
	else:
		return x * fact(x-1)