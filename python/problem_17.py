def number_to_words(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if 1 <= num < 10:
        return ones[num]
    elif 10 <= num < 20:
        return teens[num - 10]
    elif 20 <= num < 100:
        return tens[num // 10] + ones[num % 10]
    elif 100 <= num < 1000:
        if num % 100 == 0:
            return ones[num // 100] + "hundred"
        else:
            return ones[num // 100] + "hundredand" + number_to_words(num % 100)
    elif 1000 <= num < 10000:
        if num % 1000 == 0:
            return ones[num // 1000] + "thousand"
        else:
            return ones[num // 1000] + "thousand" + number_to_words(num % 1000)


allwords = ''.join(number_to_words(i) for i in range(1, 1001))
print("Solution is: " + str(len(allwords)))
