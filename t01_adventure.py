######################################################################
# Author: Jhonny Sontay, Phun Mualcin      TODO: Change this to your names
# Username: Maualcinp, sontayvicentej              TODO: Change this to your usernames
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.


direction = input("Which direction would you like to go? [North/South/East/West]" )

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.
sleep(delay*3)
print("")
print("")
print("It seems like you will be here a while.")
print("You see two doors in front of you. One is made of wood. It looks like it is about to fall off.")
print("The other door is just plants. All you gotta do is walk through and you're on the other side. ")
print("There is also a doorway with no door. ")
choice= input("Where will you go? [Wood/Plant/No door]   ")
if choice == "Wood":
    print("As you push the door open, it falls off. ")
    print("The loud noise wakes up the polar bear sleeping inside. It then proceeds to devour you with salt.")
    dead = True
elif choice == "Plant":
    print("You brush the plants to the side and walk through the doorway.")
    print("This opens up a secret path. You follow this path for hours.")
    print(" You somehow ended up at the same doorways that you encountered earlier.")

elif choice == "No door":
    print(" You walk through the doorway and you see a faint light in the distance. You run to this light.")
    print("You discover a chest. You open the chest and find food and water in the chest!.")
    print("After eating, you continue to walk on and eventually find the Exit. ")
    print("You are free!")
if dead==True:
    print("You have been eaten by the polar bear!")
    quit()

# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
