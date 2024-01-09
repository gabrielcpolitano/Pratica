# Import the library random
import random

# Create a function to choose a random word from a predefined list
def choose_word():
    words = ["python", "hangman", "programming", "computer", "science", "challenge"]
    return random.choice(words)

# Create a function to display the current state of the word, revealing guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main function for the Hangman game
def hangman():
    secret_word = choose_word()             # Choose a secret word
    guessed_letters = []                    # Lis to store guessed letters
    attempts = 6                            # Number of allowed attempts

    print("Welcome to Haangman!")
    print(display_word(secret_word, guessed_letters))  # Display initial state of the word

    while True:
        guess = input("Guess a letter: ").lower()   # Get user input for a letter

        # Validate the input
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                attempts -= 1
                print("Incorrect guess. Attempts remaining", attempts)
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_word(secret_word, guessed_letters))  # Display the updated state of the word

        # Check for winning condition
        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You guessed the word", secret_word)
            break

        # Check for losing condition
        if attempts == 0:
            print("Sorry, you ran out of attempts. The word was", secret_word)

# Run the Hangman game
hangman()


