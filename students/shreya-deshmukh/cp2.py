#problem 1
def ask_prompt(p):
 while true:
    p=input("enter...")
    if p=="":
        print("cant be empty")
    else:
            return (p)
 ask_prompt()

 #problem2
def marks(i):
    while True:
        i=int(input("enter marks"))
        if i.isdigit():
            return (i)
            print("enter correct marks ")
            marks() 

#problem 3
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


#problem 4
def collect_one_subject():
    name = ask_text("Subject name: ")
    m1 = ask_mark("  Mark 1 (0-100): ")
    m2 = ask_mark("  Mark 2 (0-100): ")
    m3 = ask_mark("  Mark 3 (0-100): ")

    return (name, m1, m2, m3)
