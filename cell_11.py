from collections import Counter

def analy(t):
    return list(Counter(t).items())

vals = []
while True:
    inp = input("Enter val (or 'stop'): ")
    if inp.lower() == 'stop':
        break
    vals.append(inp)

tup = tuple(vals)
print(analy(tup))