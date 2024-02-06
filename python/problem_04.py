def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]


max_palindrome = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if is_palindrome(str(i * j)):
            max_palindrome = max(max_palindrome, i * j)
print(max_palindrome)
