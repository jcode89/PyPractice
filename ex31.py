print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
		print "Crawling around faceless, what do you do?"
		print "1. Feel around for the cheese cake."
		print "2. Crawl away like a crazy."
		
		crazy = raw_input("> ")
		
		if crazy == "1":
			print "The bear picks you up and rips you in half. Good job!"
		elif crazy == "2":
			print "You slam right into a brick wall. OUCH!"
		else:
			print "Ninjas appear out of the void and reap your soul."
	
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
		print "Your arms work though! What do you do?"
		print "1. Use those hands to flee."
		print "2. Go for the cheese cake."
		
		serious = raw_input("> ")
		
		if serious == "1":
			print "Not quite fast enough. The bear tore your arms clean off."
		elif serious == "2":
			print "Really?! Still going after the cake? DEAD!"
		else:
			print "Wow okay the bear does speak! You are let go."
			print "When you leave you see two new doors. Which do you choose? 1 or 2?"
			
			n_door = raw_input("> ")
			
			if n_door == "1":
				print "A giant snake with a monocle reading a book about owls. What will you do?"
				print "1. Ask him about his book."
				print "2. Steal his book."
				print "3. Tell the snake you love owls."
				
				snake = raw_input("> ")
				
				if snake == "1":
					print "Tough luck. He hates questions and injects you with venom."
				elif snake == "2":
					print "Wow okay that was dumb, he just consumed you."
				elif snake == "3":
					print "Boy oh boy are you lucky. He related to your story."
				else:
					print "Great now you have to listen to all of his books forever."
					
			elif n_door == "2":
				print "A field filled with Foxy Knowledge seekers. What do you do?"
				print "1. Walk with them as they search the planet for all things knowledge."
				print "2. Try and talk to one of them."
				
				foxy = raw_input("> ")
				
				if foxy == "1":
					print "They accept you, but you are being watched. No wrong moves young one."
				elif foxy == "2":
					print "The screech and the giant Owl of Wisdom swoops down silently killing you."
				else:
					print "So %s was a secret. They show you the path home." % foxy
					
			else:
				print "Door %s opens up to the void, a violent chain reaction occurs and you are sucked from the portal to your ultimate demise." % n_door
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You star into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
		print "Alas, two new doors. You have just enough of your faculties left to choose one."
		
		doors = raw_input("> ")
		
		if doors == "1":
			print "This jello mind allows you to see through the static that lies beyond the door. What do you do?"
			print "1. Follow the white noise past the door."
			print "2. Scream as loud as you can."
			
			noise = raw_input("> ")
			
			if noise == "1":
				print "You went in, but now what? The noise ultimately consumes you as it was really another Cthulhu mind trick."
			elif noise == "2":
				print "The park ranger that was looking for the bear comes and finds you screaming and crying and saves your life."
			else: 
				print "Death is swift and painless."
		
		elif doors >= "2":
			print "Waves of light crash into your eyes burning them furiously before all calms and you are left kneeling before the hornet queen."
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		print "You're now blind but you can hear someone in the background. Is that real? What do you do?"
		print "1. Follow the voice."
		print "2. Scream out."
		
		stalk = raw_input("> ")
		
		if stalk == "1":
			print "The trail is very painful but you were right in following the voice. Merlin has restored your vision."
			print "Now what do you do with these two new doors? Choose one obviously!"
			
			merlin = raw_input("> ")
			
			if merlin == "1":
				print """
				You walk through door 1 and the smell of sulphur consumes your olfactory senses. Your eyes meltaway and all you hear is
				Merlin laughing in the background.
				"""
			elif merlin >= "2":
				print "This door leads to freedom, a mysterious anti magic barrier blocks Merlin from stopping you. Good Job."
				
			
		elif stalk == "2":
			print "Wrong move, the bear behind door number one finds you and kills you."
			
		else:
			print "Cthulhu Always wins!"
	
else:
	print "You stumble around and fall on a knife and die. Good job!"