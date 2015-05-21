from sys import argv

# This unpacks the input that was entered into argv
# at the command line and assigns the input to variables
script, first, second, third = argv
more = raw_input("Type more things!\n ")


print '''
The script is called: %r
	\nYour first variable is:%r
	\nYour second variable is:%r
	\nYour third variable is:%r
	\nYour fourth variable is:%r
	''' % (script, first, second, third, more)





