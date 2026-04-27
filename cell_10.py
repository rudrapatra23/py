def item_counts():
    n = int(input("Enter N: "))
    items = []
    for _ in range(n):
        items.append(input())

    checked = []
    for i in range(len(items)):
        if items[i] not in checked:
            count = 0
            for j in range(len(items)):
                if items[i] == items[j]:
                    count += 1
            print(f"{items[i]} -> {count}")
            checked.append(items[i])

    unique = checked
    for i in range(len(unique)):
        for j in range(len(unique) - 1 - i):
            if unique[j] > unique[j+1]:
                unique[j], unique[j+1] = unique[j+1], unique[j]
    print(unique)

item_counts()