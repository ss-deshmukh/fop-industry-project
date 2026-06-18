#cp2 -->1]ask text
def ask_text(prompt):
    while True:
        text=input(prompt)
        if text=="":
            print("cant be empty try again !")
        else:
            return text
            
#cp2 -->2]ask marks
def ask_mark(prompt):
    while True:
        text=input(prompt)
        if not text.isdigit():
            print("please enter a whole number !")
            continue
        mark=int(text)
        if 0<=mark<=100:
            return mark
        else: #sai
            print("mark must be between 0 and 100 !")
            
#cp2 -->3]ask yes or no
def ask_yes_no(question):
    while True:
        answer=input(question)
        if answer=="y":
            return True
        elif answer=="n":
            return False
        else:
            print("please type y or n !")
            
#cp2 -->4]collect imformatiom for 1 sub
def collect_one_subject():
    name=ask_text("subject name --> ")
    m1=ask_mark("Marks 1 (0-100) --> ")
    m2=ask_mark("Marks 2 (0-100) --> ")
    m3=ask_mark("Marks 3 (0-100) --> ")
    return (name,m1,m2,m3)
