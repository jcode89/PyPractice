# We define a function cheese_and_crackers and have it accept 
# two variables cheese_count and boces_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# We indent four spaces and have the function print out 
	# how much cheese, how many boxes and then
	# Just two more lines
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# Here we run our function giving it two numbers directly.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Here we run our function  after assigning two new variables
# values. 
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# We put both of those variables inside the parentheses of our function
# and run it.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# Here we are doing math inside of the parentheses of our function
# The responses to the math being done will be the arguments we will
# see when we run it.
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# Here we take our variables we created earlier and add new amounts to them
# What we will see is the answers to the math being done.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def weather(rain_count, temp):
	print "It rained %d inches." % rain_count
	print "It was %d degrees out today." % temp
	print "That is crazy weather!\n"
	
print "One way to run our function"
weather(20, 200)

print "second way"
weather(20*100, 650/50)

print "Third way!"
rain = 400
sun = 12000

weather(rain, sun)

print "fourth way!"
weather(rain * sun, sun / rain)

print "fifth way!"
new_var = int(raw_input())
new_var2 = int(raw_input())

weather(new_var, new_var2)

print "Sixth way!"
weather(new_var * 20, new_var2 / 50)

print "seventh way!"
weather(rain + new_var, sun + new_var2)

print "Eight way"
weather(rain + 10, sun + 20)

print "Ninth way!"
weather(rain**2, sun**2)

print "The tenth way!"
weather(36 % 2, 25 % 2)