jii#problem 1 
def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Can't be empty — try again.")
subject = ask_text("Subject name: ")
print(subject)

#problem 2 
def ask_mark(prompt):
    while True:
        text = input(prompt)
        if not text.isdigit():
            print("Please enter a whole number.")
        elif 0 <= int(text) <= 100:
            return int(text)
        else:
            print("Mark must")

#problem 3
def collect_one_sub():
    name = ask_text("Sub name: ")
    m1 = ask_mark("  Mark 1 (0-100) ")
    m2 = ask_mark("  Mark 2 (0-100) ")
    m3 = ask_mark("  Mark 3 (0-100) ")
    return (name, m1, m2, m3)

    return("mark",85,90,78)

#problem 4 
def ask_yes_no(q):
    while True:
        a = input (q)
        if a == ("y"):
            return True
        elif a == ("n"):
            return False
        else:
            print('Please type "y" or "n".')
result = ask_yes_no("Add another subject? (y/n): ")
print(result)


#problem 5

def collect_all_sub():
    sub = []

    sub.append(collect_one_sub())

    while len(sub) < MAX_SUB:
        if ask_yes_no("Add another sub ? (y/n): "):
            sub.append(collect_one_sub())
        else:
            break

    if len(sub) == MAX_SUB:
        print("Maximum 5 sub reached.")

    return sub


#problem 6

def print_menu():
    print(" MENU ")
    print("1. Add Subject")
    print("2. View Report")
    print("3. Clear Data")
    print("4. Exit")

print_menu()


#problem 7

def print_h(h):
    if len(h) == 0:
        print("No h yet.")
    else:
        print(" Session H ")
        for i in range(len(h)):
            print(f"[{i + 1}] {h[i]}")
        print("-")

h = ["Added 1 subject(s)", "Viewed report"]

print_h(h)


#problem 8

def print_menu():
    print("1. Add subjects")
    print("2. View report")
    print("3. View history")
    print("4. Exit")
print_menu()

def print_history(history):
    if len(history) == 0:
        print("No history yet.")
    else:
        for i in range(len(history)):
            print(f"[{i+1}] {history[i]}")
            print("-")
history=["added 1 subject(s)","viewed report"]
print_history(history)

