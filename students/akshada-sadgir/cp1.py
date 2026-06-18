# CP1
pass_mark=35
distinction_mark=75
def average_of_three(m1,m2,m3):
    avg=(m1+m2+m3)/3
    return round(avg,1)
def classify_result(avg):
    if avg<pass_mark:
        return "fail"
    elif avg>=distinction_mark:
        return "distinction"
    else:
        return"pass"
def letter_grade(avg):
    if avg>=90:
        return"A"
    elif avg>=80:
        return"B"
    elif avg>=70:
        return"C"
    elif avg>=60:
        return"D"
    else:
        return"F"
def format_marks(m1,m2,m3):
    return f"{m1},{m2},{m3}"
#CP2
def ask_prompt(p):
 while true:
    p=input("enter...")
    if p=="":
        print("cant be empty")
    else:
            return (p)
 ask_prompt()
def marks(i):
    while True:
        i=int(input("enter marks"))
        if i.isdigit():
            return (i)
            print("enter correct marks ")
            marks()
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
def collect_one_subject():
    name = ask_text("Subject name: ")
    m1 = ask_mark("  Mark 1 (0-100): ")
    m2 = ask_mark("  Mark 2 (0-100): ")
    m3 = ask_mark("  Mark 3 (0-100): ")

    return (name, m1, m2, m3)
