#problem1
def average_of_three(m1, m2, m3):
    return round((m1 + m2 + m3) / 3, 1)

print(average_of_three(85, 90, 78))  
print(average_of_three(30, 28, 35))  
print(average_of_three(40, 55, 70))
#problem2
def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
print(letter_grade(86.6))  
print(letter_grade(53.0))  
print(letter_grade(93.0))  
#problem3
pass_mark = 35
distinction_mark = 75
def classify_result(avg):
    if avg >= distinction_mark:
        return "DISTINCTION"
    elif avg >= pass_mark:
        return "PASS"
    else:
        return "FAIL"

print(classify_result(84.3))
#problem4
def ask_mark(prompt):
    while True:
        try:
            mark = int(input(prompt))

            if 0 <= mark and mark <= 100:
                return "mark"
            else:
                print("Mark between 0 and 100")

        except ValueError:
            print("enter a whole number.")
ask_mark(46)
#problem5
def ask_text(prompt):
    while True:
        text = input(prompt)
        
        if text != "":
            return "text"
        else:
            return"Can't be empty — try again."
ask_text("a")
#problem6
def ask_yes_no(question):
    while True:
        answer = input(question)

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print('Please type "y" or "n".')

result = ask_yes_no("Continue? (y/n): ")
print(result)
#problem7
def collect_all_subjects():
    subjects = []
    while True:
        name = input("Subject name: ")
        m1 = int(input("Mark 1: "))
        m2 = int(input("Mark 2: "))
        m3 = int(input("Mark 3: "))
        subjects.append((name, m1, m2, m3))

        more = input("Add another subject? (y/n): ")
        if more == "n":
            break
    return subjects
subjects = collect_all_subjects()
print(subjects)
#problem8
def build_subject_row(name, m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    if avg >= 75:
        grade = "A"
        result = "DISTINCTION"
    elif avg >= 40:
        grade = "C"
        result = "PASS"
    else:
        grade = "F"
        result = "FAIL"
    return f"{name:<16} | {m1:>3} | {m2:>3} | {m3:>3} | {avg:>4.1f} | {grade:^5} | {result}"
row = build_subject_row("Maths", 85, 90, 78)
print(row)
#problem9
def build_subject_row(name, m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    if avg >= 40:
        grade = "P"
        result = "PASS"
    else:
        grade = "F"
        result = "FAIL"
    return f"{name:<10} {m1:>3} {m2:>3} {m3:>3} {avg:>5.1f} {grade:^5} {result}"
def print_report(subjects):
    print("GRADE REPORT")
    print("------------------------------")
    total = 0
    for s in subjects:
        name, m1, m2, m3 = s
        print(build_subject_row(name, m1, m2, m3))
        total += (m1 + m2 + m3) / 3
    print("------------------------------")
    print("Overall Avg:", total / len(subjects))
subjects = [
    ("Maths", 85, 90, 78),
    ("Physics", 30, 28, 35)
]
print_report(subjects)
#problem10
def print_menu():
    print("==== MENU ====")
    print("1. Add Subject")
    print("2. View Report")
    print("3. Search Subject")
    print("4. Exit")
print_menu()
#problem11
def print_history(history):
    if len(history) == 0:
        print("No history yet.")
    else:
        print("--- Session History ---")
        for i in range(len(history)):
            print(f"[{i + 1}] {history[i]}")
        print("----------------------")
history = []
print_history(history)  
history.append("Added 1 subject(s)")
history.append("Viewed report")
print_history(history)  
