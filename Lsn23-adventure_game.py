"""
File: adventure_game.py
Author: Bryce Woodland
Date: 11/6/2022
Purpose: Have the user play an adventure game. 
"""
# Choice 1: Sprint 
choice1 = input("You're a young kid living in a small town. Nothing exciting ever happens. However, this particular morning you wake up to a loud sound. You briefly check outside your window and discover your neigbors acting strange. They are all walking single file into the woods. Do you SPRINT to the woods first to see what they are up to or do you DRIVE to your friend Claire's house and bring her along?\n")
if choice1.lower() == 'sprint':
    choice2a = input ("You decide to hurry and get to the woods before everyone else. As you do the sound that woke you up gets louder and you see bright ligts. Do you KEEP walking towards the lights or do you HEAD home?\n")
    if choice2a.lower() == 'keep':
        choice3a = input('As you edge your way closer to the lights you notice a green figure. Do you TALK to them or do you WARN everyone of what you saw?\n')
        if choice3a.lower() == 'talk':
            print('The alien grabs you and throws you into the spaceship! They then devour you!')
        elif choice3a.lower() == 'warn':
            print('All your neighbors run back to their homes! The whole town is safe. You are declared a hero!')
    elif choice2a.lower() == 'head':
        choice3b = input('As you are making your way back to your house you encounter your sibling. They insist that you follow them into the woods with the others. Do you STILL continue to your house or do you TURN around and join them?\n')
        if choice3b.lower() == 'still':
            print('Wise decision! You are safe from an alien abduction.')
        if choice3b.lower() == 'turn':
            print('As you walk back with your sibling. You notice that a group of green aliens begin surrounding you. You have been hypnotized by them.')
    else:
        print('You did not enter a valid option.')

# Choice 2: Drive
elif choice1.lower() == 'drive':
    choice2b = input("You make it to your friend Claire's house but recognize that no one is home. Do you ENTER or LEAVE?\n")
    if choice2b.lower() == 'enter':
        choice3c = input("Inside Claire's house you notice a note siting on her desk. Do you READ it or do you IGNORE it?\n")
        if choice3c.lower() == 'read':
            print('You find a note written by Claire warning you not to go to the woods. She tells you aliens have come to abduct everyone in the town. She tells you where her hideout is and has given you directions there. You head there and are safe.\n')
        elif choice3c.lower() == 'ignore':
            print("You decide not to hone into Claire's privacy. You never see her again.")
    elif choice2b.lower() == 'leave':
            choice3d =input('You head back home. All your neighbors and family members have disappeared. You are unaware of what has happened. Do you SEARCH for them or do you SLEEP?\n')
            if choice3d.lower() == 'search':
                print("As you walk through the woods you stumble upon several bodies. You hear a sound above you and can't believe your eyes. A spaceship zooms back to outerspace.")
            if choice3d.lower() == 'sleep':
                print('You go back to your house and fall asleep. You are safe from any aliens. However, everyone has gone missing and you now live in a ghost town.')
    else: 
        print('You did not enter a valid option.')
else:
    print('You did not enter a valid option.')

