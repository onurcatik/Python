import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

def roll_dice(number_of_dice):
    dice= []
    total = 0
    for _ in range(number_of_dice):
        roll = random.randint(1,6)
        dice.append(roll)
        total += roll
    return dice, total

def display_dice(dice):
    for line in range(5):
        for die in dice:
            print(dice_art[die][line], end = " ")
        print()

if __name__ == "__main__":
    number_of_dice =int(input("How many dice would you like to roll?"))
    dice ,total = roll_dice(number_of_dice)
    display_dice(dice)
    print(f"Total: {total}")