import random

hand = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

def win(score, player_name): # Win function for modularity and to simplify code
    score += 1
    print(f"You played {player} and computer played {computer}. {player_name} won!\nPlay again or type quit to exit game.")
    return score

while True: # Added while loop to be able to let user input without having to run program again
    player = input("Will you play rock, paper, or scissors?\nType quit to exit game and see your score.\n")

    if player.lower() in hand: # User input works regardless of upper or lower case
        computer = random.choice(hand)

        if player.lower() == computer: # Universal tie condition message to simplify code
            print(f"You played {player} and computer played {computer}. It's a tie!\nPlay again or type quit to exit game.")
        elif player.lower() == 'rock': # Will refactor these win conditions to simplify code and allow for more hand options
            if computer == 'scissors':
                player_score = win(player_score, "You")
            else:
                computer_score = win(computer_score, "Computer")
        elif player.lower() == 'paper':
            if computer == 'rock':
                player_score = win(player_score, "You")
            else:
                computer_score = win(computer_score, "Computer")
        elif player.lower() == 'scissors':
            if computer == 'paper':
                player_score = win(player_score, "You")
            else:
                computer_score = win(computer_score, "Computer")

    elif player.lower() == "quit": # Lets the user quit the game and view their final score
        print(f"""
        Game over! Your final score is:
        Player score: {player_score}
        Computer score: {computer_score}
        Thanks for playing!
        """)
        break

    else:
        print("Invalid input. Please enter rock, paper, or scissors. Type quit to exit game.")
