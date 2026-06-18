#problem1
def average_of_three(m1, m2, m3):
    return round((m1 + m2 + m3) / 3, 1)

print(average_of_three(85, 90, 78))  
print(average_of_three(30, 28, 35))  
print(average_of_three(40, 55, 70)) 
#problem
def ask_text(prompt):
    while True:
        text = input(prompt)
        
        if text != "":
            return "text"
        else:
            return"Can't be empty — try again."
ask_text("a")
#problem2
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
