import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice: ")

    if player == computer:
        print("It's a tie!")

    elif (player == "rock" and computer == "scissors") \
            or (player == "paper" and computer == "rock") \
            or (player == "scissors" and computer == "paper"):
        print("You win!")

    else:
        print("You lose!")

    play_again = input("Play Again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("Thank you for playing!")
