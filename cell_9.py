def process_list():
    n = int(input("Enter N: "))
    l = []
    for i in range(n):
        l.append(int(input()))

    for i in range(n):
        l[i] = l[i] * l[i]

    for i in range(n // 2):
        temp = l[i]
        l[i] = l[n - 1 - i]
        l[n - 1 - i] = temp

    if len(l) > 0:
        mx = l[0]
        mn = l[0]
        for x in l:
            if x > mx: mx = x
            if x < mn: mn = x

        res = []
        mx_done = False
        mn_done = False
        for x in l:
            if x == mx and not mx_done:
                mx_done = True
                continue
            if x == mn and not mn_done:
                mn_done = True
                continue
            res.append(x)
        print(res)

process_list()