from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


nat_numbers = []
curr_number = 0
max_divisors = 0
while max_divisors <= 501:
    curr_number = curr_number + 1
    nat_numbers.append(curr_number)

    summed = sum(nat_numbers)
    max_divisors = len(factors(summed))

print("Solution is: " + str(summed))
