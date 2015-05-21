#Sets the variable to a string of string formatters (%r)
#Remember they print out anything.
formatter = "%r %r %r %r"

#The print function calls our variable and tells the formatter to use 1234
print formatter % (1,2,3,4)
#Calls the print function, tells the formatter (%r) to use the strings given.
print formatter % ("one", "two", "three", "four")
#Calls the print function and tells the formatter to use the given boolean values
print formatter % (True, False, False, True)
#Calls the print function and tells the formatter to use the variable (formatter)
print formatter % (formatter, formatter, formatter, formatter)
#Calls the print function and that in turn calls upon our variable and then
#sets the each string formatter to these new strings
#They will print out on one line because of the comma (,)
print formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)