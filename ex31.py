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
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
	
else:
	print "You stumble around and fall on a knife and die. Good job!"