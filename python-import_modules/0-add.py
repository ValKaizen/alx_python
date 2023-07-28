# File: main.py

a = 1
b = 2

# Importing the function from add_0.py
from add_0 import add

# Calculate the result using the imported function
result = add(a, b)

# Print the formatted output
print("{} + {} = {}".format(a, b, result))

# Additional code outside the if __name__ == "__main__": block
print("This code will be executed regardless of import or direct execution.")
