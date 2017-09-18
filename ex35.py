from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	#if "0" in next or "1" in next: 
	#Note - I can't figure out how the statement(above) works.
	if next.isdigit():
		how_much = int(next)
	else:
		print("Man, learn to type a number.")
		how_much = int(raw_input("> "))

	if how_much >= 0 and how_much < 50:
		print "Nice, you're not greedy. You win!"
		exit(0)
	elif how_much < 0:
		dead("That's impossible!")	
	else:
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your legs off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I don't know how to do that."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever... stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		print "I didn't understand that. Let's try this again.\n"
		cthulhu_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()



