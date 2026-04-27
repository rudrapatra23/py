n = int(input('Enter number: '))
s, p = 0, 1
while n > 0:
    rem = n % 10
    s += rem
    p *= rem
    n //= 10
print('Is Spy number:', s == p)