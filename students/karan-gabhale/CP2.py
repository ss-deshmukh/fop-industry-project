#CP2
def ask_text():
    while True:
        sub_name = input("Enter subject name?-")
        if sub_name == "":
            print("Can't be empty. Try again.")
        else:
            return(sub_name)
            break
    
def ask_marks(): 
    while True: 
        user_input = input("Enter your marks 1-100: ") 
        if user_input.isdigit(): 
            return(user_input)
            break
        else: 
            print("Enter whole number only")


def ask_y_n(i):
    while True:
        user_input=input(i)
        if user_input == "y":
            return(True)
            break
        elif user_input == "n":
            return(False)
            break
        else:
            print("type only y/n only")


def collect():
    TN=ask_text()
    AM1=ask_marks()
    AM2=ask_marks()
    AM3=ask_marks()
    return(TN,AM1,AM2,AM3)

