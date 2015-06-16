from sys import exit

def basement():
	exit(0)

def cthulhuRoom():
	exit(0)

def forestRoom():
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