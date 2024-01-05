def calculate_bmi(weight, height):
    # Convert height from centimeters to meters
    height_in_meters = height / 100

    # Calculate BMI using the formula
    bmi = weight / (height_in_meters ** 2)
    return bmi

# Get user input for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

# Call the BMI calculation function
bmi_result = calculate_bmi(weight, height)

# Display the result
print(f"Your BMI is: {bmi_result:.2f}")

# Interpret the BMI result
if bmi_result < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi_result < 25:
    print("Your weight is normal")
elif 25 <= bmi_result < 30:
    print("You are overweight.")
else:
    print("You are obese.")