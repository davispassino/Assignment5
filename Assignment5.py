#Here is where my game begins:
print("\nWelcome to Rock Paper Scissors!")
desired_rounds = int(input("How many rounds would you like to play?: "))

#This is where my game verifies you have entered an odd number:

while desired_rounds % 2 == 0 or desired_rounds <=0:
    print ("Sorry, you must enter a positive odd number!")
    desired_rounds = int(input("Enter the amount of rounds you would like to play: "))
    
#Here is where I have defined my functions:

choice_options = ["rock","paper","scissors"]
player_wins = 0
computer_wins = 0
rounds_played = 0

def computer_function():
    import random
    computer_choice = random.choice(choice_options)
    print(f"The computer chose {computer_choice}")
    return computer_choice

def player_function():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    while player_choice not in choice_options:
              print("Sorry, enter a valid response")
              player_choice = input("Enter rock, paper, or scissors: ").lower()
    return player_choice

def choose_winner(computer_choice, player_choice):
    if computer_choice == player_choice:
        print("Tie!")
        return "tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        return "win"
    elif player_choice == "paper" and computer_choice == "rock":
        print("You won!")
        return "win"
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        return "win"
    else:
        print("You lost!")
        return "loss"

#Here is where my program runs the game loop and counts each win/loss:

while rounds_played < desired_rounds:
    print(f"\nRound {rounds_played + 1}")
    player_choice = player_function()
    computer_choice = computer_function()

    winner = choose_winner(computer_choice, player_choice)

    if winner == "win":
        player_wins += 1
        rounds_played +=1

    elif winner == "loss":
        computer_wins += 1
        rounds_played += 1
    else:
        print("This round doesn't count.")

#Here is the game summary:

print(f"\nScore:\nYou: {player_wins}\nComputer: {computer_wins}")

if player_wins > computer_wins:
    print("\nYou won the game!")

elif computer_wins > player_wins:
    print("\nThe computer won the game!")

print("Thanks for playing!\n")