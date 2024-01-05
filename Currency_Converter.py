def convert_to_reais(amount, exchange_rate):
    # Perform the conversion
    converted_amount = amount * exchange_rate
    return converted_amount

# Get user input for amount in dollars and exchange rate
amount_in_dollars = float(input("Enter the amount in dollars: "))
exchange_rate = float(input("Enter the exchange rate (1 USD to BRL): "))

# Call the conversion function
amount_in_reais = convert_to_reais(amount_in_dollars, exchange_rate)

# Display the result
print(f"${amount_in_dollars:.2f} is equal to {amount_in_reais:.2f} Brazilian reais")