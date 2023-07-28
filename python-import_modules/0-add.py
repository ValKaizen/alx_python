# File: main.py

a = 1
b = 2

from add_0 import add

# Calculate the result using the imported function
result = add(a, b)

# Print the formatted output
output =" {} + {} = {}\n".format(a, b, result)

# Additional code outside the if __name__ == "__main__": block
#output += "This code will be executed regardless of import or direct execution."
print(output)
