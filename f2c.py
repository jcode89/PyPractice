# Define a function converter with an argument of f
def converter(f):
    # Easily do the math and save the response to variable c
    c = (f -32) * 5/9
    # using float() makes sure c is a decimal.    
    return float(c)

# Prompt the user to enter a number and we turn the number to a decimal using float
# Everything entered using input() is a string,
# Therefore it has to be converetd.	
a = float(input("Enter degrees in Fahrenheit: "))

# We use string formatting to print out the result of calling converter using our variable a.
print(("The degrees in Celsius are: %f") % converter(a))