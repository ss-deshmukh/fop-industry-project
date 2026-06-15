Write a function countdown(n) that uses a while loop to count down from n to 1, printing one number per line, then prints Liftoff!.
def countdown(n):
    while n >= 1:
        print(n)
        n -= 1
    print("Liftoff!")
