#Sets the variable x equal to the string and allows the string to be formatted with %d
#%d allows integers to be added in.
x = "There are %d types of people." % 10
#Sets the variable binary equal to a string
binary = "binary"
#Sets the variable do_not equal to a string
do_not = "don't"
#Sets the variable y equal to a string and has string formatter %s
#%s allows strings to be added into the given string.
y = "Those who know %s and those who %s." % (binary, do_not)

#Both of these functions print out the variables x and y.
print x
print y

#These two print functions also print out x and y but use the string formatter %r and %s
#Using %r prints out whatever it is told no matter what. %s only prints a string
#Both become embedded in the new string and print out as one whole string
print "I said: %r." % x
print "I also said: '%s'." % y

#The variable hilarious is set equal to a boolean value False
hilarious = False
#Sets the new variable joke_evaluation equal to a string with the formatter %r that way 
#the variable hilarious will be printed out no matter what. It is a boolean value not a string, hence why %r is used.
joke_evaluation = "Isn't that joke so funny?! %r"

#Prints out the string and tells the %r to use the value given to hilarious.
print joke_evaluation % hilarious

#Variable w is given a string
w = "This is the left side of..."
#Variable e is given a string
e = "a string with a right side."

#Print takes both variables and their values and, since they are both strings, they get concatenated
#That means they were added together and now make one whole string.
print w + e

#In python, along with most other languages, you can add strings as well as numbers.
#Adding numbers returns a whole new value, while adding strings does too, only it is the first string connected to the second string
#That is called concatenating the strings. It forms a new string, but both parts are still visible
#Adding numbers returns a new value in which neither former part is visible.