# Exercise 2:
# We have used input(str) during the lecture. Write a script using the functions
# from Exercise 1 to ask the user which conversion he/she want to do. Then the
# user should enter the measurement values he/she wants to convert.

# CONSTANS

# 1. WEIGHT

POUNDS_PER_STONE = 14
KG_PER_POUND = 0.45359237

# 2. LENGTH

METERS_PER_MILE = 1609.34

# 3. LIQUID

LITERS_PER_UK_PINT = 0.568261

# IMPERIAL -> METRIC

def imperial_to_metric_weight():
    stones = int(input("Enter stones -> "))
    pounds = int(input("Enter pounds -> "))
    kilograms = (stones * POUNDS_PER_STONE + pounds) * KG_PER_POUND
    print(f"{stones} stones, {pounds} pounds = {kilograms} kilograms")

def imperial_to_metric_length():
    miles = float(input("Enter miles -> "))
    meters = miles * METERS_PER_MILE
    print(f"{miles} miles = {meters} meters")

def imperial_to_metric_liquid():
    pints = float(input("Enter pints -> "))
    liters = pints * LITERS_PER_UK_PINT
    print(f"{pints} pints = {liters} liters")

# METRIC -> IMPERIAL

def metric_to_imperial_weight():
    kilograms = float(input("Enter kilograms -> "))
    total_pounds = kilograms / KG_PER_POUND
    stones = int(total_pounds // POUNDS_PER_STONE)
    pounds = total_pounds % POUNDS_PER_STONE
    print(f"{kilograms} kilograms = {stones} stones, {pounds} pounds")

def metric_to_imperial_length():
    meters = float(input("Enter meters -> "))
    miles = meters / METERS_PER_MILE
    print(f"{meters} meters = {miles} miles")

def metric_to_imperial_liquid():
    liters = float(input("Enter liters -> "))
    pints = liters / LITERS_PER_UK_PINT
    print(f"{liters} liters = {pints} pints")

# MAIN PROGRAM

def validInput(options):
    print(">> Select your option:")

    for index, option in enumerate(options):
        print(f"{index + 1} - {option}")
    
    userInput = int(input("Enter your choice -> "))

    if userInput < 1 or userInput > len(options):
        return validInput(options)

    return userInput

def main():
    conversionOptions = ["Imperial to Metric", "Metric to Imperial"]
    conversionInput = validInput(conversionOptions)
    
    measureOptions = ["Weight", "Length", "Liquid"]
    measureInput = validInput(measureOptions)

    if conversionInput == 1:
        if measureInput == 1:
            imperial_to_metric_weight()
        elif measureInput == 2:
            imperial_to_metric_length()
        else:
            imperial_to_metric_liquid()
    else:
        if measureInput == 1:
            metric_to_imperial_weight()
        elif measureInput == 2:
            metric_to_imperial_length()
        else:
            metric_to_imperial_liquid()

main()