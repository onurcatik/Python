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

for question in questions:
    print("\n" + "-" * 50)
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
            score += 1
            print("Correct")
    else:
         print(f"Incorrect! the correc answer is {answers[question_number]}")
    question_number += 1

print("\n" + "=" * 50)
print("Quiz Results")
print("=" * 50)

print("Correct Answers:", end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print("Your Guesses: ", end= " ")
for guess in guesses:
    print(guess, end= " ")
print()

score_percentage = int((score/len(questions))*100)
print(f"Your score is: {score_percentage}%")