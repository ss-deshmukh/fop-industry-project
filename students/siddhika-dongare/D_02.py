def ask_text(prompt):
    while True:
        text = input(prompt)
        if text != "":
            return text
        print("Can't be empty — try again.")

subject = ask_text("Subject name: ")
print(subject)
