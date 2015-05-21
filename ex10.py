#Escape Sequences and String Formatters

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
new_line = "This is \"How\" we do it \npunk!"
new_line2 = 'How is this one? \'Apples\''
tile = "\nWhat is with those new tiles?"


a = 252.675
#The string formatter %s or %r will print out the float in variable a and execute the escape
b = "\n %s"   % a
sent = "\nAmount of time taken to run six blocks: %s seconds" % b




print tabby_cat
print persian_cat 
print backslash_cat
print fat_cat
#When you use the string formatter %r with an escape like \n (New line)
#Python will only execute the string formatter not the escape.
print "Try out this one: %r" % new_line
print "%r" % new_line2
#Using the %s string formatter, python will execute both the formatter and the escape
print "%s, %s" % (new_line, new_line2)
print tile
print "%s" % sent

#%r prints the raw data, exactly what you typed.
#%s prints out the string how you wanted it to print.