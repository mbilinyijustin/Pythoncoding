import random


def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! 📉")
            elif guess > number_to_guess:
                print("Too high! 📈")
            else:
                print(f"🎉 Congratulations! You guesses it in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no):").lower()
        if again not in ("yes", "y"):
            print("Thanks gor playing! 👋")
            break

if __name__ == "__main__":
    main()