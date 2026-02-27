import random

def hangman():
    words = ["python", "java", "kotlin", "javascript"]
    word_to_guess = random.choice(words)
    guessed_word = ["_" for _ in word_to_guess]
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\n" + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
            if "_" not in guessed_word:
                print("\n" + " ".join(guessed_word))
                print("Congratulations! You guessed the word.")
                break
        else:
            attempts -= 1
            print("Wrong guess!")

    if attempts == 0:
        print(f"Game over! The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()