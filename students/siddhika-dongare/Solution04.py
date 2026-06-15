#problem1
def countdown(n):
    while n >= 1:
        print(n)
        n = n - 1
    print("Liftoff!")

# Example
countdown(5)

#problem2
def first_multiple(n, start):
    x = start

    while True:
        if x % n == 0:
            break
        x = x + 1

    return x

# Example
print(first_multiple(5, 12))


#problem3
def print_triangle(height):
    row = 1
    while row <= height:
        print("*" * row)
        row += 1

# Example
print_triangle(5)

#problem4
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

#problem5
import random

secret = random.randint(1, 100)

print("I am thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("🎉 Correct! You guessed the number.")
        break
