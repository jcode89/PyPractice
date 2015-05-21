#This just prints out the string entered.
print "I will now count my chickens:"

#All math follows the order or operations, or PEMDAS, if there is more than one operation to complete.
#In this sequence 30 is divide by 6 then added to 25. If you run the code it should return 30.0
#It will return the number 30.0 because we have the sequence wrapped in the float() function.
print "Hens", float(25 + 30 / 6)
#This sequence, also wrapped in a float() function, multiplies 25 and 3 and then divides it by four,
#But the % operator or a modulo finds the remainder of that division. 
#So in this case 25 * 3 is 75 and 75 % 4 is 3. Why 3? 
# 75 / 4 is 18.75, .75 = 3/4. After you do that it will - 3 from 100.
print "Roosters", float(100 - 25 * 3 % 4)

#This also just prints the string entered.
print "Now I will count the eggs:"

#Another order of operations sequence.
#Remember PEMDAS, so first you do the modulo(%) and /(Division). Note: Modulo finds the remainder, but
#must do division to do so.
# 4 % 2 and 1 /4 go first than after you get those answers you add the rest from left to right.
print float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

#Prints a string.
print "Is it true that 3 + 2 < 5 - 7?"

#This returns a boolean value, either true or false.
#Unless wrapped in the float() function, than it is either 0.0 or 1.0
#Note: It does the math first addidng and subtracting than checks in the first is less than (<) the other.
print 3 + 2 < 5 - 7

#Prints an entered string and then does the actual math, returning a decimal, or float() value.
print "What is 3 + 2?", float(3 + 2)
#This does the same as the code above.
print "What is 5 - 7?", float(5 - 7)

#Just printing another string. 
print "Oh, that's why it's False."

#So is this one. Just printing another string that is.
print "How about some more."

#This set of code prints out a string and the boolean value, either true or false, of the given operation.
print "Is it greater?", 5 > -2
#This one checks if it is greater than or equal to.
print "Is it greater or equal?", 5 >= -2
#This checks if it is less than or equal to.
print "Is it less or equal?", 5 <= -2