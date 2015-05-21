def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# PEMDAS
# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
# (30 + 5) + (78 - 4) - (90 * 2) * ((100 / 2) / 2)
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# This problem I wrote on my own (35 * 2) * (20 - 4) + (60 / 2) 
print "Another new puzzle!"

how = add(multiply(multiply(age, 2), subtract(20, 4)), divide(60, 2))

print "That becomes: ", how, "Do you know it by hand?"