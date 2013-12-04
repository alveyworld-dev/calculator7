#Brandon H. , Luis C. , Igor J. , Nathen V.

def pow(base, power):
	"""We take the power and show it and each power return the base"""
	total = 1
	# it will now poduce a list of number 1 to power+1
	for number in range(power):
	#now we take each of range and times it with the base
			total = total * base
			
	return total		
			
#print pow(5, 6)


def ln(x):
	""" We frist our x and then we divide it with e untill it > e, and count how many times it take"""
	#Number assgined names
	total = 0
	e=2.7183
	tempX = x
	#Count how many time it take for x / e until it is less then e.
	for number in range(x):
		if tempX > e:
			tempX = tempX/e
			total = number
	return total
#print ln(50)