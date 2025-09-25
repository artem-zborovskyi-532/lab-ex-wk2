# Exercise 4:
# Write a function that takes the age (int) and rate (the heart rate as an int) as
# parameters and prints a description of a person's training zone based on his or
# her age and training heart rate. The zone is determined by comparing rate
# with the person's maximum heart rate m:

# Interval range                Training Zone
# rate ≥ 0.9 m                  Interval training
# 0.7 m ≤ rate < 0.9 m          Threshold training
# 0.5 m ≤ rate < 0.7 m          Aerobic training
# rate < 0.5 m                  Couch potato

# The maximum heart rate in beats per minute is given by the formula:
# m = 208 − 0.7 age

ageInput = int(input("Enter your age -> "))
heartRateInput = int(input("Enter heart rate -> "))

def determineTrainingZone(age:int, heartRate:int):
    maxHeartRate = 208 - 0.7 * age
    if heartRate < 0.5 * maxHeartRate:
        print("Couch potato") 
    elif heartRate >= 0.5 * maxHeartRate and heartRate < 0.7 * maxHeartRate:
        print("Aerobic training")
    elif heartRate >= 0.7 * maxHeartRate and heartRate < 0.9 * maxHeartRate:
        print("Threshold training")
    else:
        print("Interval training")

determineTrainingZone(ageInput, heartRateInput)