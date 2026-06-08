#program 1

num = 10

unum = int(input("Guess a number between 1 to 20: "))

if unum < num:
    print("Low")
elif unum > num:
    print("High")
else:
    print("Correct")
