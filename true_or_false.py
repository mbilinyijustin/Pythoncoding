# True or False Quiz game in python

quiz = [
    {"question 1": "The Earth is flat.", "answer": "False"},
    {"question 2": "Python is a programming language.", "answer": "True"},
    {"question 3": "The sun sets in the East.", "answer": "False"},
    {"question 4": "Water boils at 100 degrees celsius.", "answer": "True"},
    {"question 5": "Humans can breathe in space without a suit.", "answer": "False"}
]

score = 0

print("Welcome to the True or False quiz\n")

for i, q in enumerate(quiz, start=1):
    print(f"Q{i}: {q['question']}")
    user_answer = input("Enter True or False: ").strip().capitalize()

    if user_answer == q["answer"]:
        print("👍 Correct!\n")
        score += 1
    else:
        print(f"☠️ Wrong! The correct answer is {q['answer']}.\n")

print(f"You score {score} out of {len(quiz)}.")