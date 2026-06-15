#problem 1
SECRET=10
def play_game():
    guess=0
    while True:
        guess=int(input("Enter your guess: "))
        guess=guess+1
        if guess>SECRET:
            print("Too high")
        elif guess<SECRET:
            print("Too low")
        else:
            print("Correct You got it in guesses tries.")
            break
play_game()
