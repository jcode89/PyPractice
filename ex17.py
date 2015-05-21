from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Using a semicolon (;) Allows you to put multiple lines of code
# On one line.
# Opens the file in the in_file variable, 
# Then reads the open file and saves the data in the variable indata.
in_file = open(from_file);indata =in_file.read()

# len(indata) tells us how many bytes the file is.
print "The input file is %d bytes long" % len(indata)
# exists(to_file) returns True or False depending on whether 
# the file saved in to_file exists.
print "Does the output file exist? %r" % exists(to_file)

# Opens/creates the second file(because we included 'w').
# writes what was in the old file to the new file.
out_file = open(to_file, 'w');out_file.write(indata)
print "Alright, all done."

# Closes both open files.
# Remember, these two are separate pieces of code on one line
# thanks to our ; (semicolon)
out_file.close();in_file.close()
