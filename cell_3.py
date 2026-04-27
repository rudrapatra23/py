n = int(input("Enter the number: "))
sum_even = 0
cur_even = 2
for i in range(n):
    sum_even += cur_even
    cur_even += 2
print(f"The sum of first {n} even number is: {sum_even}")