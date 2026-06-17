
def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Can't be empty — try again.")
subject = ask_text("Subject name: ")
print(subject)


def ask_mark(prompt):
    while True:
        text = input(prompt)
        if not text.isdigit():
            print("Please enter a whole number.")
        elif 0 <= int(text) <= 100:
            return int(text)
        else:
            print("Mark must")
