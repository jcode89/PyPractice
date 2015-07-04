ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that!"

# ten_things.split(' ') is the same as .split(ten_things, ' ')
# Call split with arguments ten_things and ' '.
# Python reads the split() function and then knows it must separate the ten_things list by one space.
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# A while loop that takes the len of our list and constantly checks to make sure it does not equal (!=) 10.
while len(stuff) != 10:
    # This is the same as save pop(more_stuff) to next_one
	# or call pop with argument more_stuff and save the result to new variable next_one.
    next_one = more_stuff.pop()
    print "Adding: ", next_one
	# This is the same as append(stuff, next_one)
	# or Call append with arguments next_one and stuff.
	# Append reads the list stuff and checks the item saved in the variable next_one and adds it to the end of stuff.
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

# stuff[1] uses the cardinal number 1 to find the second item in the list and return it to you.
print stuff[1]
# stuff[-1] uses the cardinal number -1 to find the last item in the list and return it to you.
print stuff[-1] # woah fancy!
# stuff.pop() == pop(stuff); pop reads the list stuff and removes the last item and returns it to you.
# Call pop with argument stuff.
print stuff.pop()
# ' '.join(stuff) join(' ', stuff)
# call join with arguments stuff and ' '
# join reads over the list stuff and knows that it has to bring the list together leaving only one space between words.
print ' '.join(stuff)# what? cool!
# join('#', stuff[3:5])
# Call join with arguments stuff[3:5] and '#'
# join looks over the list only focusing on the 4th and 5th word in the list and joining them together with a #.
print '#'.join(stuff[3:5]) # super stellar!
# remove(stuff, "Crows")
# or Call remove and pass it arguments stuff and "Crow"
# remove reads the list stuff and looks for the word Crows removing it from the list when it is found.
stuff.remove("Crows")
print stuff

deck = []
#while len(deck) != 52:
#    cards = raw_input("Enter in playing cards: ")
#    print "Adding: ", cards
#    deck.append(cards)
#    print "The count is %d." % len(deck)
#print "The full deck: ", deck
from random import randint
food = ["Corn", "Steak", "Chicken", "Pork", "Asparagus", "Green Beans", "Romaine", "Butter Lettuce"]
element1 = randint(0, 7)
element2 = randint(0, 7)
print "Element 1: ", food[element1]
print "Element 2: ", food[element2]

vacay_spot = ["Rome", "Guyana", "Tijuana", "San Diego", "New York", "Paris", "London", "Berlin", "Beijing"]
pick = raw_input("Pick a vacation spot: ")
if pick in vacay_spot:
    print pick
else:
    print "I said pick a real spot!"