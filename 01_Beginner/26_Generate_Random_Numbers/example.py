import random 

low=1
high=100
guesses = 0 
number_to_guess=random.randint(low, high)

while True:
    guess = int(input(f"Enter number {low} , {high} : "))
    guesses += 1

    if guess < number_to_guess:
        print((f"{guess}, low"))
    elif guess > number_to_guess:
        print(f"{guess}, high")
    else:
        print(f"{guess} is correct")
        break

print(f"This round took you {guesses} guesses")