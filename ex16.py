from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# Opens the file and 'w' allows you to write to the file.
# If 'w' is not included nothing can be done to the file except
# reading it. Also 'w' truncates the file.
target = open(filename, 'w')

#print "Truncating the file. Goodbye!"
# truncate() deletes the contents of the file.
# If you pass 'w' as a mode in open() then you don't have to print
# truncate().
#target.truncate()

print "Now I'm going to ask you for three lines."

# Saves your input to variables line1, line2, line3
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# This will write the values of our variables to the file in target.
# In order to use the %s formatter you have to nest it all within
# write() or else python thinks you want to format the write() function
target.write("%s\n%s\n%s\n" % (line1, line2, line3))


print "And finally, we close it."
target.close()