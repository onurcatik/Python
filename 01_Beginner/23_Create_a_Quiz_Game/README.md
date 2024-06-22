# Create a QUIZ GAME 

## Step 1: Declare Collections and Variables

First, we need to declare all the necessary collections and variables:

- A tuple of questions
- A 2D tuple of options
- A tuple of correct answers
- A list to store user guesses
- A variable to keep track of the score
- A variable to keep track of the current question number

### Code

```python
# Declare collections and variables
questions = (
    "How many elements are in the periodic table?",
    "Which animal lays the largest eggs?",
    "What is the most abundant gas in Earth's atmosphere?",
    "How many bones are in the human body?",
    "Which planet in the solar system is the hottest?"
)

options = (
    ("A. 118", "B. 119", "C. 120", "D. 121"),
    ("A. Ostrich", "B. Whale", "C. Eagle", "D. Platypus"),
    ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"),
    ("A. 206", "B. 205", "C. 207", "D. 208"),
    ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter")
)

answers = ("C", "A", "C", "A", "B")

guesses = []
score = 0
question_number = 0
```

## Step 2: Display Questions and Options

Next, we need to display each question along with its corresponding options. We will iterate over the `questions` tuple and print each question. For each question, we will also display the corresponding options.

### Code

```python
# Display questions and options
for question in questions:
    print("\n" + "-" * 50)
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter A, B, C, or D: ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {answers[question_number]}")
    question_number += 1
```

## Step 3: Calculate and Display Results

After all questions have been answered, we need to calculate the score and display the results. We will iterate over the `answers` and `guesses` lists to print the correct answers and the user's guesses. Finally, we will calculate the user's score as a percentage.

### Code

```python
# Calculate and display results
print("\n" + "=" * 50)
print("Quiz Results")
print("=" * 50)

print("Correct Answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Guesses:   ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int((score / len(questions)) * 100)
print(f"Your score is: {score_percentage}%")
```

## Complete Code

Here is the complete code for the quiz game:

```python
# Quiz Game in Python

# Declare collections and variables
questions = (
    "How many elements are in the periodic table?",
    "Which animal lays the largest eggs?",
    "What is the most abundant gas in Earth's atmosphere?",
    "How many bones are in the human body?",
    "Which planet in the solar system is the hottest?"
)

options = (
    ("A. 118", "B. 119", "C. 120", "D. 121"),
    ("A. Ostrich", "B. Whale", "C. Eagle", "D. Platypus"),
    ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"),
    ("A. 206", "B. 205", "C. 207", "D. 208"),
    ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter")
)

answers = ("C", "A", "C", "A", "B")

guesses = []
score = 0
question_number = 0

# Display questions and options
for question in questions:
    print("\n" + "-" * 50)
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter A, B, C, or D: ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {answers[question_number]}")
    question_number += 1

# Calculate and display results
print("\n" + "=" * 50)
print("Quiz Results")
print("=" * 50)

print("Correct Answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Your Guesses:   ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int((score / len(questions)) * 100)
print(f"Your score is: {score_percentage}%")
```

This code will create a simple quiz game in Python, allowing users to answer multiple-choice questions and receive feedback on their performance. Feel free to modify the questions, options, and answers to create your own custom quiz game.