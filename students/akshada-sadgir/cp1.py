#problem1
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
