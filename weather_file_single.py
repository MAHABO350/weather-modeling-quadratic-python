# Weather Modeling using Quadratic Equation
# File Input - Single Set

with open("input_single.txt", "r") as file:
    a = float(file.readline())
    b = float(file.readline())
    c = float(file.readline())
    t = float(file.readline())

temperature = a * t * t + b * t + c

print("Weather Modeling (File Input - Single Set)")
print("Temperature at time", t, "hours :", temperature, "°C")
