n = int(input('Enter number: '))
orig, rev = n, 0
while n > 0:
    rev = (rev * 10) + (n % 10)
    n //= 10
print('Is Palindrome:', orig == rev)