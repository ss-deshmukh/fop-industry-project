#problem 1
def classify_grade(score):
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    elif score>=60:
        print("D")
    elif score<35:
        print("F")
    else:
        print("pass")
score=int(input("Enter score:"))   
classify_grade(score)
