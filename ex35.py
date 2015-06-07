from sys import exit

def secret():
	print "You meet the Lord of the Flies and he hands you two items."
	print "A wand and a broad sword."
	print "Which do you use?"
	
	choice = raw_input("> ")
	
	if choice == "wand":
		dead("The magic back fires, you should know better!")
	elif choice == "sword":
		print "You turn on the lord and reclaim the underground!"
		exit(0)
	else:
		dead("He is tired of your antics!")

def garden():
	print "You fell through the floor and landed in the secret garden."
	print "The roses and tulips smell deliciously, but which do you pick?"
	
	choice = raw_input("> ")
	if choice == "roses":
		print "A cloud of dust puffs out of each rose and you black out."
		cthulhu_room()
	elif choice == "tulips":
		print "The magic wasp approaches you and covers your mouth leading you to a hollow in a tree."
		tree = False
		while True:
			choice = raw_input("> ")
			
			if choice == "climb":
				dead("Spiders claim your soul.")
			elif choice == "dig" and not tree:
				print "You found a tunnel very good job!"
				tree = True
			elif choice == "dig" and tree:
				dead("Wow, should have quit.")
			elif choice == "crawl" and tree:
				print "You see and entrance and crawl through."
				secret()
			else:
				print "Now you will pay!"
				cthulhu_room()
	else:
		dead("The poison flows through your veins and consumes you.")

def mad_doctor():
	print "A mysterious doctor has run to your side to help heal all wounds."
	print "He picks you up and asks what you want to do."
	print "Go in through the door or fall through the trap door."
	
	choice = raw_input("> ")
	if choice == "door":
		gold_room()
	elif choice == "trap door":
		garden()
	else:
		dead("I am not sure what you did, but, ")

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = int(raw_input("> "))
	if choice != 0:
		how_much = choice
	else:
		dead("Really?")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
	
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			print "The bear gets pissed off and chews your leg off."
			mad_doctor()
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
			
def cthulhu_room():
	print"Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else: 
		cthulhu_room()
	
	
	
def dead(why):
	print why, "good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
		

start()		