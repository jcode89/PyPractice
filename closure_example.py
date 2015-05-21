# An example of a closure in python
def addition(x):
    slack = "running outer %d" % x
    print slack
    def addition(y):
        print("running inner")
        return x + y
    return addition
# This is the first call to the function and it is running the outer function.
addition = addition(2)
# By putting 2 and 3 in add() we call the inner function and it then prints out the outer and inner.
print addition(3)

# When using closures the inner function can use variables passed to the outside function.
# The outside function runs and sets up the second function so that can be called and ran as well.
# First call to the function saves it to a variable and in this case we still need a y variable so,
# add(3) will pass three to the inner function and then allow it to return x + y.
# Once that happens everything will print out in order.