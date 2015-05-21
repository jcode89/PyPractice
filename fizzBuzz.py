def fizzBuzz(n):
	msg = [] # Creates an empty list
	# xrange() returns an object that generates the list of numbers on demand
	# More memory efficient especially when using it for loops.
	for item in xrange(1, n + 1): # Loops through our range of numbers up until n + 1
		if item % 3 == 0 and item % 5 == 0: #Condition to check in item from our range is divisible by 3 and 5
			msg.append("fizzbuzz")# Adds "fizzBuzz" to our list
		elif item % 3 == 0:# Condition to check if item from our range is divisible by 3
			msg.append("fizz")# Adds "fizz" to the list 
		elif item % 5 == 0:# Condition to check if item from our range is divisible by 5
			msg.append("buzz")# Adds "buzz" to the list
		else:
			msg.append(str(item)) # If none of the above conditions are true the number in the range
	return " , ".join(msg)        # is added on to the list. It must be wrapped in the str() function 
	#Returns our list		      # Or an error is raised.    
    # " , ".join(msg) takes away the quotes and the brackets when the list is printed out by joining
    # the words together with just a comma (,).
print fizzBuzz(100)