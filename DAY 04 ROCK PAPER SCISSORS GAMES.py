rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
game_images=[rock,paper,scissors]

selection=int(input("Welcome to the game of ROCK PAPER & SCISSORS! Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS!\n "))
computer_selection=random.randint(0,2)
if selection==0 and computer_selection==0:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("IT'S A DRAW")
elif selection==0 and computer_selection==1:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("YOU WIN")
elif selection==0 and computer_selection==2:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("YOU LOOSE")
#******************************************2ND CASE************************#
elif selection==1 and computer_selection==0:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("YOU WIN")
elif selection==1 and computer_selection==1:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("IT'S A DRAW")
elif selection==1 and computer_selection==2:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("YOU LOOSE")
##************************************************THIRD CASE***********************************##

elif selection==2 and computer_selection==0:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("YOU LOOSE")
elif selection==2 and computer_selection==1:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("YOU WIN")
elif selection==2 and computer_selection==2:
    print(game_images[selection])
    print("COMPUTER CHOOSE!\n")
    print(game_images[computer_selection])
    print("IT'S A DRAW")
else:
    print("YOU ENTERED AN INVALID ENTRY! YOU LOOSE")

    
