def coke(n):
	""" This is a simple function using a while loop to run the bottles of coke song. """
	bottle = n
	# I wrote it this way to show how the while loop works. 
	# So long as the statement (n > 0) is True the loop will run the code indented four spaces.
	# As the loop runs and n = n - 1 the number stored in n keeps going down until finally n > 0 returns False thus breaking the loop.
	while(n > 0):
		print "%d bottles of coke on the wall. %d bottles of coke.\n" % (n, n)
		n -= 1
		print "Take one down and pass it around. %d bottles of coke on the wall.\n" % n
		if n == 0:
			print "%d bottles of coke on the wall. %d bottles of coke. Go to the store buy us some more. %d bottles of coke on the wall.\n" % (n, n, bottle)
	return 
	
coke(99)
print "\n"	

def coke2(n):
	""" This is a simple function to run the bottles of coke song using a for loop. """
	for bottle in xrange(n, 0, -1):
		bottle = bottle
		print """%d bottles of coke on the wall. %d bottles of coke. \nTake one down and pass it around. 
%d bottles of coke on the wall.\n""" % (bottle, bottle, bottle -1)# bottle - 1 so that the song makes sense. The last sentence starts the new amount
		# We must set it equal to 1 so it will run.
		# If it is set equal to 0 the code would never run. The loop reaches zero and breaks before running the code.
		if bottle == 1:
			print "0 bottles of coke on the 0 bottles of coke. \nGo to the store buy us some more. %d bottles of coke on the wall" % n
	return	
coke2(99)