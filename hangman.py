
import random

words = ["python", "codealpha", "internship", "programming", "developer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

if "_" not in guessed:
    print("You win! The word was:", word)
else:
    print("Game over! The word was:", word)
