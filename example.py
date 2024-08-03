import random

options = ("rock", "paper", "scissors")

running = True

while running:
    player = None
    computer = random.choice(options)
    
    # The following block should be indented to be inside the while loop
    while player not in options:
        player = input("rock, paper, or scissors? ").lower()
    
    # This block should also be indented to be inside the while loop
    if computer == player:
        print("It's a Tie!")  # Fixed typo: "It's Tie!" to "It's a Tie!"
    elif (player == "scissors" and computer == "rock") or \
         (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock"):
        print("You Lose")  # Corrected win/lose logic
    else:
        print("You Win")

    play_again = input("Play again? (y/N) ").lower()  # Added question to input prompt and .lower() for consistency

    if play_again != "y":
        running = False

print("Thank you")
