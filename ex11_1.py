print "Age please: "
# By placing raw_input() inside of int() we turn the string entered
# into an integer, so long as numbers are used.
age = int(raw_input())
print "Height in inches please: "
height = int(raw_input())
print "Weight please: "
weight = int(raw_input())


# Metric conversion for height
new_height = height * 2.54
# Metric conversion for weight
new_weight = weight * 0.453592

# Check out the escapes and formatters used here.
print "You are %r years old, \nyour height in cm is: %r, \nyour weight in kg is: %r" %(
	age, new_height, new_weight)