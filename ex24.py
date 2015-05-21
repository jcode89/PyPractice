print "Let's practice everything."
# Escape sequences that allow you to print out a single quote (') or double quote("") without making python think you ended your string early.
# You can also print out slashes by doing \\. Or tab the text ove by \t.
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# Allows you to have a string that goes across multiple lines.
poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
# Prints out the value saved in the variable. 
# In this case it is a string.
print poem
print "--------------"

# Saves the answer to the equation in the variable five
five = 10 - 2 + 3 - 6
# A string formatter that prints out the value of five as a string.
print "This should be five: %s" % five

# A function with the argument started
def secret_formula(started):
	# Saves the value of started multiplied (*) by 500 to jelly_beans.
	jelly_beans = started * 500
	# Takes the value saved in jelly_beans and divides (/) it by 1000.
	# The value is saved in jars.
	jars = jelly_beans / 1000
	# Takes the value of jars and divides (/) it by 100.
	# This value is saved in crates.
	crates = jars / 100
	# Returns the three variables and allows them to be unpacked from the function to be used individually in the rest,
	# of the programs.
	return jelly_beans, jars, crates
	
# Creates a new variable start_point and sets it equal to ten thousand.
start_point = 10000
# Unpacks the variables that were returned at the end of the function while also passing the new variable start_point to the function.
# By doing so all of the variables will have values based on the equations in the function and the number 10000.
# By putting beans first you assign whatever value jelly_bean holds to the new variable beans.
beans, jars, crates = secret_formula(start_point)
# Uses a string formatter %d to put the value saved in start_point in the string we are printing out.	
print "With a starting point of: %d" % start_point
# Uses string formatters %d to print out the values saved in beans, jars, and crates to the string.
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# Saves a new value in start point after dividing the old value by ten.
start_point = start_point / 10

print "We can also do that this way:"
# Uses string formatters %d to assign all three variables to the string while also passing the new value of start_point to secret_formula.
# Because all three variables are returned in the function you are allowed to format the string in this manner.
print "we'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)	