# Andy Skabelund
# Assignment 4
# Calculates volume and surface area
print("Welcome to the Cuboid Calculator!")
print("Please enter values in feet.")
# Assigns length variable
length = float(input("Enter the length:"))
print(length)
# Assigns width variable
width = float(input("Enter the width:"))
print(width)
# Assigns height variable
height = float(input("Enter the height:"))
print(height)
print("Your", length, "X", width, "X", height, "cuboid has a Volume of", length * width * height, "cubic feet")
print("and a Surface Area of", (2 * length * height) + (2 * width * height) + (2 * length * width), "square feet.")
