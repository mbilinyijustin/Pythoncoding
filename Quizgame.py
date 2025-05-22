#Simple Quiz Game in python

#Questions and answers stored in a list of dictionaries.
quiz = [
    {"question": "What is the capital of France?", "options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"], "answer": "A"},
    {"question": "What is 5+7?", "options": ["A. 10", "B. 12", "C. 14", "D. 15"], "answer": "B"},
    {"question": "What wrote 'Romeo and Juliet'?", "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Jane Austen"], "answer": "C"},
]


score = 0

#Loop Through each question

for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")

print(f"\nYou got {score} out of {len(quiz)} correct.")