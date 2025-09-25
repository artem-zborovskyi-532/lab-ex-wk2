# Exercise 3:
# A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for
# postage and packaging. If an order is over £50.00, the P&P is reduced by £1.50.
# Write a function that will take the number of kilo of bananas and return the cost
# of the order in pence. Then write a script requesting the user to input the number
# of kilos for an order and print the cost of that order.

def checkout(kg):
    # CONSTANTS IN PENCE
    PRICE_PER_KG = 300
    POSTAGE_AND_PACKAGING = 499
    DISCOUNT_THRESHOLD = 5000
    DISCOUNT = 150

    total = kg * PRICE_PER_KG
    current_postal_and_packaging = POSTAGE_AND_PACKAGING

    if total > DISCOUNT_THRESHOLD:
        current_postal_and_packaging -= DISCOUNT

    total += current_postal_and_packaging
    return total

userInput = float(input("Enter the number of kilos -> "))
cost = checkout(userInput)
print(f"Total for your order: {cost} pence")