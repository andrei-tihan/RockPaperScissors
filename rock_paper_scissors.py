import random

hand = ["rock", "paper", "scissors"]
player = input("Will you play rock, paper, or scissors?")
computer = random.choice(hand)

if player.lower() in hand:
    print("Input test")
else:
    print("Please enter rock, paper, or scissors.")