import random

while True:
    player = input("enter rock, paper, scissors, or exit: ").lower()

    if player == "exit":
        print("Thanks for playing!")
        break

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    if player not in choices:
        print("invalid input")
        continue

    print(f"Computer chose: {computer}")

    if computer == player:
        print("tie")
    elif (computer == "rock" and player == "scissors") or \
         (computer == "paper" and player == "rock") or \
         (computer == "scissors" and player == "paper"):
        print("computer wins")
    else:
        print("you win")
