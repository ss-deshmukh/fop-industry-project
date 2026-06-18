def ask_text(prompt):
    while True:
        user_input=input(prompt)
        if(user_input==str("")):
            print("can't be empty ")
        else:
            return(user_input)
a = ask_text(" enter your name:")
def get_mark():
    while True:
        user_input = input("Enter mark 0-100: ")
        
        if not user_input.isdigit():
            print("Must be a whole number — try again.")
            continue
        
        mark = int(user_input)
        
        if (mark < 0 or mark > 100):
            print("Must be between 0 and 100 — try again.")
        else:
            return mark
score = get_mark()
print(f"Valid mark: {score}")
def ask_yes_no(question):
    while True:
        answer = input(question)
        
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print('Please type "y" or "n".')
ask_yes_no("enter value:" )
def collect_one_subject():

    name = ask_text("Subject name: ")
    m1 = ask_mark(" Mark 1 (0-100): ")
    m2 = ask_mark(" Mark 2 (0-100): ")
    m3 = ask_mark(" Mark 3 (0-100): ")
    return(name,m1,m2,m3)

collect_one_subjet()
