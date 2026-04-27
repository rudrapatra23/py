s_val = int(input('Start range: '))
e_val = int(input('End range: '))
for i in range(s_val, e_val + 1):
    if i < 2: continue
    p = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            p = False
            break
    if p: print(i, end=' ')
print()