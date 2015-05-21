print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." %(
	age, height, weight)

# This piece of code is the example code from the Python doc on raw_input
# It shows you that you can type a string into the parentheses.
# Typing in a string generally allows you to direct the user who is going to
# actually do the input.	
print "Type anything near the arrow, then hit enter."
s = raw_input('-->')
print s

#An example using raw_input found on stackoverflow
# Define two functions test() and other()
def test():
	print "OMG, it works..."

def other():
	print "I can call multiple functions"
	
# This will be to handle input for a function we don't have
def fail():
	print "You gave a bad function name. I only know about %s" % (
	", ".join(funcs.keys()))

# This is a dictionary - a set of keys and values.  
# Read about dictionaries, they are wonderful.  
# Essentially, I am storing a reference to the function
# as a value for each key which is the value I expect the user to ender.
funcs = {"test": test, "other": other}

# Get the input from the user and remove any trailing whitespace just in case.
target = raw_input("Function to run? ").strip()

# This is the real fun.  We have the value target, which is what the user typed in
# To access the value from the dictionary based on the key we can use several methods.
# A common one would be to use funcs[target]
# However, we can't be sure that the user entered either "test" or "other", so we can 
# use another method for getting a value from a dictionary.  The .get method let's us
# specify a key to get the value for, as wel as letting us provide a default value if
# the key does not exist.  So, if you have the key "test", then you get the reference to 
# the function test.  If you have the key "other", then you get the reference to the 
# function other.  If you enter anything else, you get a reference to the function fail.


# Now, you would normally write "test()" if you wanted to execute test.  Well the 
# parenthesis are just calling the function.  You now have a reference to some function
# so to call it, you have the parenthesis on the end.
funcs.get(target, fail)()

# The above line could be written like this instead
function_to_call = funcs.get(target, fail)
function_to_call()