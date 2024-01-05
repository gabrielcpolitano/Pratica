def is_palindrome(word):
    # Convert the word to lowercase and remove spaces
    cleaned_word = word.lower().replace(" ", "")

    # Check if the cleaned word is the same when reversed
    return cleaned_word == cleaned_word[::-1]

# Get user input
user_input = input("Enter a word: ")

# Check if the entered word is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome")