# Define variables with different data types
num = 42                  # integer
pi = 3.14159              # float
name = "John Smith"       # string
is_cool = True            # boolean
grades = [90, 85, 95]     # list of integers

# Print the values and data types of the variables
print("num =", num, "  Type:", type(num))
print("pi =", pi, "  Type:", type(pi))
print("name =", name, "  Type:", type(name))
print("is_cool =", is_cool, "  Type:", type(is_cool))
print("grades =", grades, "  Type:", type(grades))

# Manipulate the variables and print the results
print("num + 5 =", num + 5)
print("pi * 2 =", pi * 2)
print("name + ' is awesome!' =", name + " is awesome!")
print("not is_cool =", not is_cool)
print("The first grade is", grades[0])
print("The average grade is", sum(grades)/len(grades))
