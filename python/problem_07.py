def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [2, 3, 5]
count = 3
i = 7
while count < 10001:
    if is_prime(i):
        primes.append(i)
        count += 1
    i += 2

print(primes[-1])
