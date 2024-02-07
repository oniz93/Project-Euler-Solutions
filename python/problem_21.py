def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)


amicable = set()
for x in range(1, 10001):
    y = sum_of_proper_divisors(x)
    if x != y and x == sum_of_proper_divisors(y):
        amicable.add(x)
        amicable.add(y)

solution = sum(amicable)
print("Solution is: " + str(solution))
