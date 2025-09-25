# Exercise 1:
    # Imperial to Metric converter
    # a. Write a series of functions that convert weight, distance, and liquid
    # measurement from Imperial to Metric system. For example, to convert
    # weight:
        # • the function imperial_to_kg(stones, pounds) should take two
        # parameters, one for the number of stones (int), and one for the number
        # of pounds (int),
        # • The function should return the weight in Kilograms (float).
        # • For example:
        # >>> print(imperial_to_kg(10, 9))
        # 67.585263
        # >>>
    # b. For each of the functions you have defined in 1a write the reverse
    # conversion. You will need to consider:
        # • What parameter(s) the function has?
        # • What is the type of the returned value(s)

# 1. WEIGHT

POUNDS_PER_STONE = 14
KG_PER_POUND = 0.45359237

# 2. LENGTH

METERS_PER_MILE = 1609.34

# 3. LIQUID

LITERS_PER_UK_PINT = 0.568261

# IMPERIAL -> METRIC

def imperial_to_metric_weight(stones:int, pounds:int) -> float:
    kilograms = (stones * POUNDS_PER_STONE + pounds) * KG_PER_POUND
    return kilograms

def imperial_to_metric_length(miles:float) -> float:
    meters = miles * METERS_PER_MILE
    return meters

def imperial_to_metric_liquid(pints:float) -> float:
    liters = pints * LITERS_PER_UK_PINT
    return liters

# METRIC -> IMPERIAL

def metric_to_imperial_weight(kilograms: float):
    total_pounds = kilograms / KG_PER_POUND
    stones = int(total_pounds // POUNDS_PER_STONE)
    pounds = total_pounds % POUNDS_PER_STONE
    return stones, pounds

def metric_to_imperial_length(meters:float) -> float:
    miles = meters / METERS_PER_MILE
    return miles

def metric_to_imperial_liquid(liters:float) -> float:
    pints = liters / LITERS_PER_UK_PINT
    return pints