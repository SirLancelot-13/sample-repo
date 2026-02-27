import random

def word_scramble():
    words = ["python", "programming", "developer", "terminal", "game"]
    word = random.choice(words)
    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled_word = "".join(scrambled)

    print("Welcome to Word Scramble!")
    print(f"Unscramble the word: {scrambled_word}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower()
        if guess == word:
            print("Congratulations! You guessed the word.")
            break
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")

    if attempts == 0:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    word_scramble()