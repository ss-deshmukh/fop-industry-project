pass_mark=35
distinction_mark=75
# cp1 --> 1] average
def average_of_three(m1,m2,m3):
    average=(m1+m2+m3)/3
    return round(average,1)
# cp1 --> 2] classify average
def classify_average(average):
    if average<pass_mark:
        return "Failed"
    elif average>=distinction_mark:
        return "Distinction"
    else:
        return "Pass"
# cp1 --> 3] classify grade
def letter_grade(average):
    if average>=90:
        return "A"
    elif average>=80:
        return "B"
    elif average>=70:
        return "C"
    elif average>=60:
        return "D"
    else:
        return "F"
# cp1 --> 4] make string
def format_marks(m1,m2,m3):
    return f"{m1}, {m2}, {m3}"
# cp1 --> 5] improvement check
def is_improvement(old_average,new_average):
    if new_average>old_average:
        return True
    else:
        return False
