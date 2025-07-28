import random

hand = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

def win(score, player_name): # Win function for modularity and to simplify code
    score += 1
    print(f"{player_name} won! Your score is {player_score} to computer's {computer_score}. Play again or type quit to exit game.")
    return score

while True: # Added while loop to be able to let user input without having to run program again
    player = input("Will you play rock, paper, or scissors? Type quit to exit game.")

    if player.lower() in hand:
        computer = random.choice(hand)

        if player.lower() == computer:
            print(f"It's a tie! Your score is {player_score} to computer's {computer_score}. Please try again or type quit to exit game.")
        elif player.lower() == hand[0]:
            if computer == hand[2]:
                player_score += win(player_score, "You")
            else:
                computer_score += (computer_score, "Computer")
        elif player.lower() == hand[1]:
            if computer == hand[0]:
                player_score += (player_score, "You")
            else:
                computer_score += (computer_score, "Computer")
        elif player.lower() == hand[2]:
            if computer == hand[1]:
                player_score += (player_score, "You")
            else:
                computer_score += (computer_score, "Computer")

    elif player.lower() == "quit":
        print(f"""
        Game over! Your final score is:
        Player score: {player_score}
        Computer score: {computer_score}
        Thanks for playing!
        """)
        break
    else:
        print("Invalid input. Please enter rock, paper, or scissors. Type quit to exit game.")