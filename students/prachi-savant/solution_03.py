#problem1
def countdown(n):
    while n >= 1:
        print(n)
        n = n - 1
    print("Liftoff!")

countdown(5)

#problem 2
def first_multiple(n, start):
    x = start

    while True:
        if x % n == 0:
            break
        x = x + 1

    return x


print(first_multiple(5, 12))

#problem 3
def print_triangle(height):
    row = 1
    while row <= height:
        print("*" * row)
        row += 1

print_triangle(5)
