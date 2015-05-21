from sys import argv

# Unpacks the arguments entered at the command line and saves them
# to variables.
script, input_file = argv

# A function we created that reads a file when an open file is passed as
# argument f.
def print_all(f):
	print f.read()

# A function that points python to the beginning of our file
# It uses the seek function to do this.	
def rewind(f):
	# seek points to any spot in the file. If set to 0 then it goes back to the beginning.
	f.seek(0)
	
# A function designed to print out the line count and to print out the
# line associated with line count.	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
# Opens our file and saves it to a new variable current_file	
current_file = open(input_file)

print "First let's print the whole file:\n"
# Calls our print_all function and passes the argument
# current_file which is our open file.
# print_all will take our open file and read it printing
# out each line.
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# Calls our rewind function passing the argument current_file to it
# This will point python to the beginning of our file so we can 
# go through it again if we want.
rewind(current_file)

print "Let's print three lines:"

# We create a new variable current_line and set it equal to one.
current_line = 1
# We call our function print_a_line and add the arguments current_line
# and current_file.
# Current_line we just created and current_file is our open file.
# It will then print out the line and the string associated with that line.
print_a_line(current_line, current_file)

# current_line is already set to one, so doing current_line += 1 tells
# python to do current_line = current_line + 1 or 1 + 1, which gives us 2
current_line += 1
# Calling our print_a_line function again and passing the same arguments
# We will print out 2 and readline will read from the next new string which is
# string 2.
print_a_line(current_line, current_file)

# Since current_line is now equal to 2 doing current_line += 1
# is the same as doing current_line = current_line + 1 or
# 2 + 1, which will give us three
current_line += 1
# calling print_a_line for the third time will pass the same arguments,
# except current_line is now equal to three, and readline is ready to read our third string
# Which is the very next line in the text.
print_a_line(current_line, current_file)

# current_line is passed to the function print_a_line as the argument for line_count
# because it is in the place where line_count is, python sets line_count equal to whatever
# current_line is.