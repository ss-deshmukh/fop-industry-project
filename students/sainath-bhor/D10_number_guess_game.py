def guess_game():
    a=29
    tries=0
    while True:
        x=int(input("guess secret number -->"))
        if x>39:
            print("your guess is too high")
            tries=tries+1
        elif x>29:
            print("you should go little lower")
            tries=tries+1
        elif x<19:
            print("your guess is too low")
            tries=tries+1
        elif x<29:
            print("you should go little higher")
            tries=tries+1
        else: #sai
            print("correct guess you got it")
            tries=tries+1
            break
    print(f"you guess number in {tries} guesses")
guess_game()
