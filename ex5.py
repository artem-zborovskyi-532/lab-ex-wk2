# Exercise 5:
# Write a function that takes the lengths of the sides of a triangle (a, b, and c) from
# the user and then print the area of the triangle using Heron's formula. (Look up
# Heron's formula if you do not remember it.). Note, to compute xn using Python,
# you could use the function pow(x,n).

def area():
    a = float(input("Enter a -> "))
    b = float(input("Enter b -> "))
    c = float(input("Enter c -> "))

    s = (a + b + c) / 2

    areaSquared = s * (s - a) * (s - b) * (s - c)

    res = pow(areaSquared, 0.5)

    return res

print(area())