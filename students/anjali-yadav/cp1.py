# CP 1
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
# CP 2
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
# CP 3
MAX_SUBJECTS = 5

# CP1 helper functions
def average_of_three(m1, m2, m3):
    return round((m1 + m2 + m3) / 3, 1)

def get_grade(avg):
    if avg >= 80: return 'A'
    elif avg >= 70: return 'B'
    elif avg >= 60: return 'C'
    elif avg >= 50: return 'D'
    elif avg >= 40: return 'E'
    else: return 'F'

def get_result(grade):
    if grade in ['A', 'B']: return 'DISTINCTION'
    elif grade in ['C', 'D', 'E']: return 'PASS'
    else: return 'FAIL'

# 1. collect_one_subject
def collect_one_subject():
    name = input("Subject name: ")
    m1 = int(input("  Mark 1 (0-100): "))
    m2 = int(input("  Mark 2 (0-100): "))
    m3 = int(input("  Mark 3 (0-100): "))
    return (name, m1, m2, m3)

# 2. collect_all_subjects
def collect_all_subjects():
    subjects = []
    entry = collect_one_subject()
    subjects.append(entry)
    
    while len(subjects) < MAX_SUBJECTS:
        if ask_yes_no("Add another subject? (y/n): "):
            entry = collect_one_subject()
            subjects.append(entry)
        else:
            break
            
    if len(subjects) == MAX_SUBJECTS:
        print("Maximum 5 subjects reached.")
    return subjects

def ask_yes_no(prompt):
    ans = input(prompt).strip().lower()
    return ans == 'y'

# 3. build_subject_row
def build_subject_row(name, m1, m2, m3):
    avg = average_of_three(m1, m2, m3)
    grade = get_grade(avg)
    result = get_result(grade)
    return f"{name:<16}| {m1:>3} | {m2:>3} | {m3:>3} | {avg:>4.1f} | {grade:^5} | {result}"

# 4. print_report
def print_report(subjects):
    print("=" * 60)
    print(f"{'GRADE REPORT':^60}")
    print("=" * 60)
    print(f"{'Subject':<16}| {'M1':>3} | {'M2':>3} | {'M3':>3} | {'Avg':>4} | {'Grade':^5} | Result")
    print("-" * 60)
    
    total = 0
    for name, m1, m2, m3 in subjects:
        print(build_subject_row(name, m1, m2, m3))
        total += average_of_three(m1, m2, m3)
    
    print("-" * 60)
    overall_avg = round(total / len(subjects), 1) if subjects else 0
    print(f"Overall Average: {overall_avg}")
    print("=" * 60)

# 5. main
def main():
    print("=" * 40)
    print(f"{'GRADE BUDDY':^40}")
    print("=" * 40)
    subjects = collect_all_subjects()
    print_report(subjects)

main()
# CP 4
def print_menu():
    print("========================================")
    print("           GRADE BUDDY")
    print("========================================")
    print("1. Add subjects")
    print("2. View report")
    print("3. View history")
    print("4. Quit")
    print()


def print_history(history):
    if len(history) == 0:
        print("No history yet.")
    else:
        print("--- Session History ---")

        for i in range(len(history)):
            print(f"[{i + 1}] {history[i]}")

        print("----------------------")
