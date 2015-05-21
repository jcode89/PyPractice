name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
new_height = height * 2.54 # centimetres
new_weight = weight * 0.453592 # Kilograms 
print "Let's talk about %r." % name # %r will print whatever the variable is no matter what.
print "He's %r inches tall." % height
print "He's %f centimetres tall." % new_height # %f will print a float instead of a regular integer
print "He's %d pounds heavy." % weight # %d or %i both print regular integers (One's with no float)
print "Actually that's not too heavy."
print "In kilograms he is %f kilograms." % new_weight
print "He's got %s eyes and %r hair" % (eyes, hair) #%s prints a string if you use %r it will print but with quotes
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
#How you list the variables at the end in the parentheses matters if you want them to show up correctly in the string.
print "If I add his height in centimetres %f, and his weight in kilograms %F, I get %f." % (
    new_height, new_weight, new_height + new_weight)