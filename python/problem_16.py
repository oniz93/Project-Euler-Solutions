def calculate_sum_of_digits(base, power):
    number = base ** power
    return sum(int(digit) for digit in str(number))


print(f"Solution is: {calculate_sum_of_digits(2, 1000)}")
