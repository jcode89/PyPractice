###http://www.artima.com/weblogs/viewpost.jsp?thread=240808###
#The site points to python decorators.
#class entryExit(object):
#	def __init__(self, f):
#		self.f = f
#	def __call__(self):
#		print "Entering", self.f.__name__
#		self.f()
#		print "Exited", self.f.__name__
		
#@entryExit
#def func1():
#	print "inside func1()"
	
#@entryExit
#def func2():
#	print "inside func2()"
	
#func1()
#func2()
# Creates a function (entryExit) and has it accept an argument (f).
def entryExit(f):
	# Everything in this function always runs first.
	# Defines another new function that accepts no arguments but can use the argument accepted in the outer function
	def new_f():
		# Everything in this function always runs second.
		# Prints out Entering and the name of the function or variable passed to f.
		print "Entering", f.__name__
		# runs whatever f was. If it was a function, it will run that function. If it was a variable, well than that will run
		f()
		# Prints out the string Exited and the name of the function or variable assigned to argument f.
		print "Exited", f.__name__
	# Returns the new values in new_f that will be called when entryExit is initialized and runs.
	return new_f
	
# A decorator that gets called before a function that will use it.	
@entryExit
# This will be our f argument.
def func1():
	print "inside func1()"
	
@entryExit
# This will be our f argument.
def func2():
	print "inside func2()"
# Took on the attributes of the decorator and has to be called in order for the decorator to run.
func1()
# Same goes for this one.
func2()
# Prints out the name of whatever func1 is.
# It should be new_f.
print func1.__name__

# A closure with no decorator used.
# everything applies the same though, outer runs first and inner can use the arguments passed to the outer.
# Since the inner and out accept two different variables, and the inner has a line of code that requires two to run.
# The function has to be called with a value set to it and then called again with another value.
def create_adder(x):
	def _adder(y):
		return x + y
	return _adder

# First call.	
add2 = create_adder(2)
add100 = create_adder(100)

# Second call.
# Like the decorators above. add2 and add100 take on the attributes of the create_adder function.
print add2(50)
print add100(50)