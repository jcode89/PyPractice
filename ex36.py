from sys import exit
from math import sqrt

def gameRoom():
	print """
		That was such a bad choice, you have been tricked!
		"""
	cthulhuRoom()

def orcRoom():
	print """
		They are swinging and mad as you enter their territory!\n
		There aren't many options just fight or flee.\n
		Which do you choose?
		"""
	orc = raw_input("> ").lower()
	
	if orc == "fight":
		dead("\t\tDid you think you had a chance?")
	else:
		dead("\t\tThere is no escape!")

def beeRoom():
	print """
		They are buzzing and humming and headed straight for you!\n
		Do you run away, or scream, or fight?
		"""
	bee = raw_input("> ").lower()
	
	if bee == "run":
		print "\t\tYou shouldn't have done that!"
		print "\t\tConsumed!"
		exit(0)
	elif bee == "scream":
		print "\t\tMerlin appears and saves you."
		merlin()
	elif bee == "fight":
		dead("\t\tThey sting you mercilessly!")
	else:
		print "\t\tJason has caught up to you!"
		dead("\t\tThe bees are the least of your problems!")
	
def merlin():
	answrs = []
	rspns = []
	print """
		He sees you and smiles asking you what you would like from him.\n
		When you tell him you want to go home he grins.\n
		"One more test." Merlin tells you.
		"""
	print '\t\t"Tell me the square root of 64, 144, 225, and 400, in order."'
	first = sqrt(64)
	answrs.append(first)
	second = sqrt(144)
	answrs.append(second)
	third = sqrt(225)
	answrs.append(third)
	fourth = sqrt(400)
	answrs.append(fourth)
	
	wizard = True
	while True:
		print "First answer?"
		ans1 = int(raw_input())
		rspns.append(ans1)
		print "Second answer?"
		ans2 = int(raw_input())
		rspns.append(ans2)
		print "Third answer?"
		ans3 = int(raw_input())
		rspns.append(ans3)
		print "fourth answer?"
		ans4 = int(raw_input())
		rspns.append(ans4)
	
	
		if answrs == rspns:
			print "\t\tYou're freedom awaits young one."
			exit(0)
		elif answrs != rspns and wizard:
			print "\t\tThat isn't right start over!"
			wizard = False
		elif answrs != rspns and not wizard:
			dead("\t\tYour failure is an embarrassing!")
	
def basement():
	print """
		You have made it into the basement. Good job!\n
		You're not out yet though!\n
		Go to the window, or the trap door, or you could try screaming.
		"""
	
	basement = raw_input("> ").lower()
	
	if basement == "scream":
		dead("\t\tThat was bad choice. The police are too late.")
	elif basement == "trap door":
		cthulhuRoom()
	elif basement == "window":
		gameRoom()
	

def cthulhuRoom():
	print """
		The lair of the mighty Cthulhu!\n
		You may regret what you have just done!
		Especially since you could be here for a long time.
		"""
	cthulhu = raw_input("> ").lower()
		
	if cthulhu == "lemons":
		print "\t\tThe citrus burns your eyes as the might roar of laughter thunders!"
		cthulhuRoom()
	elif cthulhu == "run":
		dead("\t\tThe psychosis will consume you!")
	else:
		print "\t\tWhat is happening!"
		freddyRoom()
	
def forestRoom():
	print """
		You have made it to the forest!\n
		You're not safe yet though!\n
		You are at a fork of sorts, and you can\n
		either go straight, left, or right.
		"""
		
	forest = raw_input("> ").lower()
		
	if forest == "straight":
		print """Jason was still chasing after you, but you
		manage to shimmy up a tree."""
		print "\t\tMerlin is sitting at the very top."
		merlin()
	elif forest == "left":
		print "\t\tYou encounter a horde of deadly bees!"
		beeRoom()
	elif forest == "right":
		print "\t\tYou have run into the clan of Orcs!"
		orcRoom()
	else:
		print "What? No, the forest consumes your soul!"
		exit(0)

def michaelMyersRoom():
	print """
		It's Halloween!\n
		A certain estranged man is wondering the house you have found yourself in.\n
		Yes, that is a very sharp knife he is carrying.\n
		What are you going to do?
		Will you call the police, fight, or are you brave enough to summon Cthulhu.
		"""
	michael = raw_input("> ").lower()
		
	if michael == "call the police":
		basement()
	elif michael == "fight":
		dead("\t\tReally a man with a knife?")
	else:
		cthulhuRoom()

def jasonRoom():
	print """
		Why does that sign say Crystal Lake?\n
		Don't tell me...\n
		You've wandered into Crystal Lake and now have to deal with\n
		Mr. Jason Voorhees himself.\n
		There is not much to do, run, fight or hide?
		"""
	scared = True
	while True:
		jason = raw_input("> ").lower()
	
		if jason == "run":
			print "\t\tJason is no where to be found. Good work!"
			forestRoom()
		elif jason == "fight":
			dead("\t\tAre you insane!")
		elif jason == "hide" and scared:
			print "\t\tHe knows you're in here."
			scared = False
		elif jason == "hide" and not scared:
			dead("\t\tHe found you this time!")
		else:
			print "\t\tYou're own scream is the last thing you hear."
			exit(0)
	
def freddyRoom():
	print """
		The house is quiet, but something isn't right. \n
		Freddie's going to get you!\n
		Do you run, or fight, or is this all a dream\n
		and maybe you have to wake up.
		"""
	freddy = raw_input("> ").lower()
	
	if freddy == "run":
		dead("\t\tInvading your dreams, the infamous claws make themselves known!")
	elif freddy == "fight":
		print "\t\tHe lives in your nightmares, fighting is useless, but you do manage to get out."
		michaelMyersRoom()
	elif freddy == "wake up":
		print "\t\tYou're nightmare is only getting worse"
		jasonRoom()
	else:
		freddyRoom()

def dead(message):
	print message + " You will not survive!"
	exit(0)

def start():
	print """
		Welcome! \n 
		I see you have learned your way around!\n
		You have to choose a path of course, left, right, or center.\n
		Choose wisely my friend.
		"""
	choice = raw_input("> ").lower()
	
	if choice == "left":
		freddyRoom()
	elif choice == "center":
		jasonRoom()
	elif choice == "right":
		michaelMyersRoom()
	else:
		dead("\t\tThe ground gave way to Dante's Inferno.")
		
start()