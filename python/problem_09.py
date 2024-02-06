found = False
for x in range(300, 1001):
    for y in range(1, x):
        for z in range(1, y):
            if x + y + z == 1000:
                if z ** 2 + y ** 2 == x ** 2:
                    found = True
                    print(str(x) + "*" + str(y) + "*" + str(z) + "=" + str(x * y * z))
                    break
        if found:
            break
    if found:
        break
