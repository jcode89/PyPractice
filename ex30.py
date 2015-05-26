people = 50
cars = 20 
trucks = 60

# Checks if the statement is true by seeing if the number in the cars variable is greater than the number in the peoples variable or
# if the number of trucks is less than the number of cars.
if cars > people or trucks < cars:
	# If either one is True then this print statement is run.
	print "We should take the cars."
# If the initial if statement is false than this runs.
# It checks if the number of cars is less than the number of people and the number of people is greater than cars.
elif cars < people and people > cars:
	# If both statements are True then this print statement will run.
	print "We should not take the cars."
# If neither of the first two statements evaluate to True, then this statement is run printing out the line underneath.
else:
	print "We can't decide."
	
# This statement checks to see if the number of trucks is greater than the number of cars or if the number of trucks is equal to people.
if trucks > cars or trucks == people:
	#If either one is True, this print statement runs.
	print "That's too many trucks."
# If the first is false, we go to this one.
# This checks id Trucks is less than cars or cars are less than people.
elif trucks < cars or cars < people:
	# If either evaluates to True, than this code runs.
	print "Maybe we could take the trucks."
# If both evaluate to False than this code is run.
else:
	print "We still can't decide."
	
# Checks to see if the number of people is greater than the number of trucks and if the number of cars is less than the number of trucks.
if people > trucks and cars < trucks:
	# If both evaluate to True than the print will run.
	print "Alright, let's just take the trucks."
# If it returns False, than this will run.
else:
	print "Fine, let's stay home then."