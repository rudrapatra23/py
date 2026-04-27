a = int(input('Enter first: '))
b = int(input('Enter second: '))
c = int(input('Enter third: '))
if a >= b and a >= c: res = a
elif b >= a and b >= c: res = b
else: res = c
print('Largest:', res)