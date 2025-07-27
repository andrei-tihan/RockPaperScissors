import random

hand = ["rock", "paper", "scissors"]
computer = random.choice(hand)

while True:
    player = input("Will you play rock, paper, or scissors? Type quit to exit game.")

    if player.lower() in hand:
        print("Input test")
    elif player.lower() == "quit":
        print("Game over, thanks for playing!")
        break
    else:
        print("Invalid input. Please enter rock, paper, or scissors. Type quit to exit game.")