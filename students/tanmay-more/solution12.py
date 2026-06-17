#problem no 1
def sum_to_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


print(sum_to_n(5))   
print(sum_to_n(1))   
print(sum_to_n(10))

#problem no 2
def times_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

times_table(7)
