print "You walk down the trail of suns and you come to a fork in the road. Do you go right or left?"

trail = raw_input("> ").lower()

if trail =="right":
	print "Masked by many shrubs it is hard to pass, but you make it through only to find weapons."
	print "What shall you do? Pick up the chain or pick up the sword?"
	
	weapon = raw_input("> ").lower()
	
	if weapon == "chain":
		print "The ferocious gibbon conquers you steadfast and steals back its chains."
	elif weapon == "sword":
		print "You lean for the sword and the gibbon misses you alerting you to it's presence you swing mightily and slash it."
		print "A win for now, but as you move forward you come across the Great Owl, what do you do?"
		print "Talk to the owl."
		print "Use the sword."
		print "Type talk or sword."
		
		owl = raw_input("> ").lower()
		
		if owl == "talk":
			print "The Great Owl loves great conversation, your skills as an orator precede you. Good Job!"
		elif owl == "sword":
			print "The Great Owl is swift and your blow misses. He swoops down pecking out your eyes. Good Job."
		else:
			print "Running away without the sword was a bad idea. A ninja finds it and swiftly kills you."
	else: 
		print "The gibbon army finds you stumbling about over the weaponry and tears you limb from limb."
		
elif trail =="left":
	print "A more clear path you are left in front of a giant snorlax."
	print "What do you do."
	print "Find the pokeflute."
	print "Use physics to move him."
	print "Type flute, or physics."
	
	object = raw_input("> ").lower()
	
	if object == "flute":
		print "He awakens and immediately wants to battle."
		print "You have no pokemon though and cannot flee back."
		
	elif object == "physics":
		print "Always the better choice. You easily move him from the path but find yourself in front of another fork."
		print "Choose, right or left?"
		
		path = raw_input("> ").lower()
		
		if path == "right":
			print "A cricket swarm is clearly visible. Do you shield with your jacket and run or duck under?"
			print "Type shield or duck"
			
			move = raw_input("> ").lower()
			
			if move == "shield":
				print "You barrel through blind as a bat and are impaled by a broken tree limb. Great."
			elif move == "duck":
				print "You move past able to see a broken tree limb and duck past that into a clearing."
			else:
				print "Snorlax wakes up and kills you, because this isn't pokemon."
				
		elif path == "left":
			print "You trip over fishing line and a trap activates, an axe swings down from the heavens and slices right through you."
		else: 
			print "Okay, why didn't I think to fly away."
	else:
		print "You spent to much time thinking and the gibbon army found you."
		
else:
	print "Knives rain from the heavens and tear into your soul. You have been reaped."