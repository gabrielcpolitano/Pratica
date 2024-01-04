# Function to calculate factorial
def calculate_factorial(number):
    # Check if the number is negative
    if number < 0:
        return "Cannot calculate the factorial of a negative number"
        
    # Base case: factorial of 0 is 1 
    if number == 0:
        return 1 
    
    # Recursive case: number * factorial of the reduced number by 1 
    return number * calculate_factorial(number - 1)
    
# User prompt to enter a number
number = int(input('Enter a number to calculate the factorial: '))

# Calculate and print the factorial
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}")