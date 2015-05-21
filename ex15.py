# Imports the argv function from the sys module
from sys import argv

# saves the arguments entered in at the command line into variables
# They are being unpacked.
script, filename = argv

# Creates a variable txt and then opens the file saved in the variable filename
# Once the file is open you are able to read or write or append the file.
txt = open(filename)

# Uses the %r formatter to print the filename you entered
print "Here's your file %r:" % filename
# Calls the open file saved in the txt variable and applies the read() function
# Then prints out the contents of the file.
print txt.read()

# This is how you do the same thing, but using raw_input instead
# Creates a variable file_again and then waits for the user to
# enter the filename so it can save it to the variable.
print "Type the filename again:"
file_again = raw_input("> ")

# Creates a new variable txt_again and the calls upon the open() function
# to open the file saved in file_again.
txt_again = open(file_again)

# Calls the read() function and prints out the contents of the file.
print txt_again.read()

# These two statements close the file you opened earlier on
# You always need to close your files so you don't leave them open in the 
# garbage collector.
txt.close()
txt_again.close()

# Side note: When you start python in the command line and you 
# want to open a file, save it in a variable and save the file as
# a string first.
# Then, you can open it and read it.