# Here's some new strange stuff, remember type it exactly.
#Variable days set to the string "Mon Tue Wed Thu Fri Sat Sun"
days = "Mon Tue Wed Thu Fri Sat Sun"
#Variable months set to the string of months listed bu each one is printed on a new line
#as indicated by \n
months= "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#Prints out the string and calls the variable to print out its string as well
print "Here are the days: ", days
#print prints out the string given plus the contents of the variable months
print "Here are the months: ", months

#An example of how to print out over multiple lines.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
"""
#The code below is just some fun code found in ex10.
#while True:
#	for i in ["/", "-", "|", "\\", "|"]:
#		print "%s\r" % i,
		