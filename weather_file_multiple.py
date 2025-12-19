# Weather Modeling using Quadratic Equation
# File Input - Multiple Sets

print("Weather Modeling (Multiple Sets)")

with open("input_multiple.txt", "r") as file:
    for line in file:
        a, b, c, t = map(float, line.split())
        temperature = a * t * t + b * t + c
        print("Time:", t, "hours -> Temperature:", temperature, "°C")
