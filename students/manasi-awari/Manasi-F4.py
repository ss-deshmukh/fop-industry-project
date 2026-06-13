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

print(classify_grade(95))
print(classify_grade(85))
print(classify_grade(75))
print(classify_grade(65))
print(classify_grade(45))
