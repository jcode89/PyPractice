# The First exercise on http://www.ling.gu.se/~lager/python_exercises.html
#I wrote these for Python 2XXX
# Write a function max() that takes two arguments and returns the larger one.

def max(a,b):
    if a > b:
        return a
    elif b > a:
        return b
        
        
print max(654, 96)

# This is the second challenge from that site.
# define a function max_of_three() that takes three integers and returns the largest.
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
        
print max_of_three(5001, 5002, 5000)

# This is the third challenge.

# Define a function that calculates the length of a given string.

def len_string(string):
    total = 0
    for letter in string:
        total += 1
    return total
        
string = raw_input("Enter any string: ")# This is all that needs to be changed to convert to Python 3XXX
print len_string(string)