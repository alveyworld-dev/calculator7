#Brandon Bench, Baylen Pentz, Malone Wright

def add(*n):
	"""This function takes in any numbers and returns the sum of them."""
	sum = 0
	for x in n:
		sum += int(x)
	return sum
	
def sub(x,*y):
	"""This function takes in a starting number and then any numbers and subtracts them."""
	base = x
	for x in y:
		base -= x
	return base
	
def opp(x):
	"""This function takes a number and returns the opposite of it."""
	return x * -1
	

