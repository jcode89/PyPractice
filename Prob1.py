# Project Euler Problems.
# A function that runs through a list of numbers under i and adds together multiples of
# three or five.
def three_five(i):
	# Creates the variable total and sets equal to zero
	total = 0
	# Loops through a list of numbers created by range.
	# It starts at 1 and stops at the value of i.
	# Each item is stored in the variable num.
	for num in xrange(1, i):
		# Checks if the current value in num is divisible by three or five.
		if num % 3 == 0 or num % 5 == 0:
			#If it is then num is added to total which then becomes the new value of total.
			#The loop goes and does this until it reaches the end of the list of numbers.
			total += num
			#print num
	# Returns the value saved in total after the for loop has run completely.
	return total
print three_five(1000), "\n"

#for item in xrange(1, 10):
	#print item


# This is actually Problem 2 in Project Euler
# It is a function that creates a list of Fibonacci numbers while adding all of
# the even ones together.	
def fib(n):
	#Two variables one set to zero the other to one.
	a = 0
	b = 1
	# Creates and empty list.
	result = []
	# Creates a variable that is set equal to zero.
	new_result = 0
	# Loops through the next lines of code so long that the value of b is less than the value of n.
	while b < n:
		# Takes the current value of b and adds it to our empty list (result).
		result.append(b)
		# Stores the current value of b in a so it can be used to add to the new value of b. 
		# I.E. 0 + 1 = 1; 1 + 1 = 2; 1 + 2 = 3; 2 + 3 = 5
		# That will happen so long as the b value is less than the n value.
		a, b = b, a + b
		# Checks if the b value is divisible by two/even.
		if b % 2 == 0:
			# If it is it will be added to our variable new_result which starts out with a value of zero.
			new_result += b
	# Prints out our list of Fibonacci numbers after the while loop breaks. 	
	print result, "\n"
	# Returns the new value saved in new_result.
	return new_result
print fib(4000000), "\n"

def square_sum(b):
	total = 0
	# Loops through the list created by xrange(0, b + 1).
	# That list will go as high as b plus (+) 1.
	# The item is then saved in num so that the code that comes next can be executed
	# using the value stored in num.
	# Then it grabs the next item and does it again.
	for num in xrange(0, b + 1):
		#Same as typing total = total + (num**2)
		# (num**2) Is num squared.
		total += (num**2)
	return total
def sum_square(b):
	total = 0
	for num in xrange(0, b + 1):
		total += num
		
	return total**2
	
def difference(a, b):
	total = 0
	# If they are not on the proper side of the - (minus) sign then the total will be
	# negative.
	total = sum_square(a) - square_sum(b)
	return total
	
print square_sum(10), "\n"
print sum_square(10), "\n"
print difference(10, 10), "\n"