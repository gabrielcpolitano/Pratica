# Ask the user to enter a word
user_input = input("Enter a word: ")

# Initialize a variable to count the number of vowels
count = 0

# Iterate through each character in the user-provided word
for char in user_input:
    # Check if the character is a vowel (the letters 'a', 'e', 'i', 'o', 'u' in lowercase)
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        # If it is a vowel, increment the count
        count += 1

# Display the result
print(f"The number of vowels in the word '{user_input}' is: {count}")

