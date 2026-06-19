MAX_SUBJECTS = 5


def average_of_three(m1, m2, m3):
    return round((m1 + m2 + m3) / 3, 1)

def get_grade(avg):
    if (avg >= 80):
        return ('A')
    elif (avg >= 70):
        return ('B')
    elif (avg >= 60):
        return ('C')
    elif (avg >= 50):
        return ('D')
    elif (avg >= 40): 
        return ('E')
    else: 
        return('F')

def get_result(grade):
    if grade in ['A', 'B']: 
        return ('DISTINCTION')
    elif grade in ['C', 'D', 'E']: 
        return ('PASS')
    else:
        return ('FAIL') 
    
def collect_one_subject():
    name = input("Subject name: ")
    m1 = int(input("  Mark 1 (0-100): "))
    m2 = int(input("  Mark 2 (0-100): "))
    m3 = int(input("  Mark 3 (0-100): "))
    return (name, m1, m2, m3)

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


def build_subject_row(name, m1, m2, m3):
    avg = average_of_three(m1, m2, m3)
    grade = get_grade(avg)
    result = get_result(grade)
    return f"{name:<16}| {m1:>3} | {m2:>3} | {m3:>3} | {avg:>4.1f} | {grade:^5} | {result}"


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

