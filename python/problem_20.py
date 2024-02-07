import math

# Calculate the factorial
f = math.factorial(100)
# make a list for each digit
f = [int(d) for d in str(f)]

# sum up with numpy
print("Solution is: " + str(sum(f)))
