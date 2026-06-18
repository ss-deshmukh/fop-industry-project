#cp1 problem
def avg(n1, n2, n3):
    a = (n1 + n2 + n3) / 3
    return a

def result(a):
    if a >= 75:
        print("distinction")  
    elif a >= 35:
        print("pass")
    else:
        print("fail")
        
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
def format_marks(m1, m2, m3):
    return f"{m1},{m2},{m3}"
mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

print("-" * 30)


formatted = format_marks(mark1, mark2, mark3)
print(f"Entered Marks: {formatted}")


calculated_avg = avg(mark1, mark2, mark3)
print(f"Average Score: {calculated_avg:.2f}")


grade_letter = classify_grade(calculated_avg)
print(f"Grade: {grade_letter}")


print("Status: ", end="")
result(calculated_avg)

#cp2 problem
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

#CP3

Max_subject=5
def collect_all():
    subject=[]
    entry=collect()
    subject.append(entry)
    print(subject)
    while len(subject)<Max_subject:
        if ask_y_n("Enter another subject-"):
            ele = collect()
            print(ele)
            subject.append(ele)
            print(subject)
        else:
            break
    if len(subject)==Max_subject:
        return("maximum subject reached")
    return(subject)
collect_all()
