fib_sequence = [0, 1]
last_number = 1
i = 2
while True:
    last_number = fib_sequence[i-1] + fib_sequence[i-2]
    if last_number > 4000000:
        break
    fib_sequence.append(last_number)
    i += 1
print(sum([x for x in fib_sequence if x % 2 == 0]))
