n = int(input('Enter number: '))
orig, s, d, t = n, 0, 0, n
while t > 0:
    d += 1
    t //= 10
t = n
while t > 0:
    s += (t % 10) ** d
    t //= 10
print('Is Armstrong:', s == orig)