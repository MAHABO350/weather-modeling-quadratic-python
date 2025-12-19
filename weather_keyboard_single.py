# Weather Modeling using Quadratic Equation
# Keyboard Input - Single Set

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter constant c: "))
t = float(input("Enter time in hours: "))

temperature = a * t * t + b * t + c

print("Weather Modeling (Keyboard Input)")
print("Temperature at time", t, "hours :", temperature, "°C")
