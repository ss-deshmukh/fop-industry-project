#problem1
def ask_text(prompt):
    while True:
        text = input(prompt)
        
        if text != "":
            return "text"
        else:
            return"Can't be empty — try again."
ask_text("a")
